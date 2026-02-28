#!/usr/bin/env python3
"""
Google Fonts Injector & Font Class Optimizer
=============================================
Scans a Vue + Vite SPA project for Tailwind/UnoCSS font-['...'] declarations,
validates them against Google Fonts, injects <link> tags into index.html,
and optionally optimizes redundant font class usage.
"""

import argparse
import os
import re
import shutil
import sys
import urllib.request
import urllib.error
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCAN_EXTENSIONS = {".vue", ".tsx", ".jsx", ".html", ".css", ".ts", ".js", ".scss", ".less", ".pcss"}

# Regex to match font-['FontName'], font-["FontName"], font-[&quot;FontName&quot;]
FONT_CLASS_PATTERN = re.compile(
    r"""font-\["""                   # font-[
    r"""(?:['"]|&quot;)"""           # opening quote: ' or " or &quot;
    r"""([A-Za-z0-9_\s]+?)"""       # font name (captured)
    r"""(?:['"]|&quot;)"""           # closing quote
    r"""\]""",                       # ]
    re.VERBOSE
)

# For matching the full class token (e.g. font-['Inter']) in source files
FONT_CLASS_TOKEN_PATTERN = re.compile(
    r"""font-\[(?:['"]|&quot;)[A-Za-z0-9_\s]+?(?:['"]|&quot;)\]"""
)

INJECTION_MARKER_START = "<!-- Google Fonts Auto-Injected -->"
INJECTION_MARKER_END = "<!-- /Google Fonts Auto-Injected -->"

SYSTEM_FONTS = {
    # Generic CSS families
    "sans-serif", "serif", "monospace", "cursive", "fantasy",
    "system-ui", "ui-sans-serif", "ui-serif", "ui-monospace", "ui-rounded",
    # Common system fonts (lowercased for comparison)
    "arial", "helvetica", "helvetica neue", "times new roman", "times",
    "georgia", "verdana", "tahoma", "trebuchet ms", "courier new",
    "lucida console", "lucida sans", "lucida grande",
    "segoe ui", "consolas", "menlo", "monaco", "dejavu sans",
    # CJK system fonts
    "microsoft yahei", "pingfang sc", "pingfang tc", "hiragino sans",
    "hiragino sans gb", "noto sans cjk", "simsun", "simhei",
    "wenquanyi micro hei", "apple color emoji", "segoe ui emoji",
    "noto color emoji", "ms gothic", "ms mincho", "yu gothic",
}

# Root CSS file candidates (relative to project_root)
ROOT_CSS_CANDIDATES = [
    "src/styles/app.less",
    "src/style/app.less",
    "src/style/var.less",
]


# ---------------------------------------------------------------------------
# Phase 1: Scan & Extract
# ---------------------------------------------------------------------------

def scan_fonts(project_root: Path, scan_dir: str) -> Dict[str, List[str]]:
    """
    Scan all relevant files and return {normalized_font_name: [file_paths_where_found]}.
    """
    target = project_root / scan_dir
    if not target.is_dir():
        print(f"⚠️  Scan directory not found: {target}")
        return {}

    font_files: Dict[str, List[str]] = {}

    for root, _dirs, files in os.walk(target):
        # Skip node_modules, dist, .git, etc.
        rel_root = os.path.relpath(root, project_root)
        if any(skip in rel_root.split(os.sep) for skip in ["node_modules", "dist", ".git", ".output", ".nuxt"]):
            continue

        for fname in files:
            fpath = Path(root) / fname
            if fpath.suffix.lower() not in SCAN_EXTENSIONS:
                continue

            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            matches = FONT_CLASS_PATTERN.findall(content)
            for raw_name in matches:
                # Underscore → space (Google Fonts convention)
                name = raw_name.replace("_", " ").strip()
                rel_path = str(fpath.relative_to(project_root))
                font_files.setdefault(name, []).append(rel_path)

    return font_files


# ---------------------------------------------------------------------------
# Phase 2: Filter system fonts
# ---------------------------------------------------------------------------

def filter_system_fonts(font_map: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Remove fonts that are system/generic and don't need Google Fonts."""
    return {
        name: paths
        for name, paths in font_map.items()
        if name.lower() not in SYSTEM_FONTS
    }


# ---------------------------------------------------------------------------
# Phase 3: Validate against Google Fonts
# ---------------------------------------------------------------------------

def validate_google_font(font_name: str) -> bool:
    """Check if a font exists on Google Fonts by sending a HEAD request."""
    url_name = font_name.replace(" ", "+")
    url = f"https://fonts.googleapis.com/css2?family={url_name}"
    req = urllib.request.Request(url, method="HEAD")
    req.add_header("User-Agent", "Mozilla/5.0 (google-fonts-injector)")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return False


def validate_fonts(font_map: Dict[str, List[str]]) -> Tuple[Dict[str, List[str]], List[str]]:
    """
    Validate all fonts against Google Fonts API.
    Returns (valid_font_map, invalid_font_names).
    """
    valid = {}
    invalid = []
    for name, paths in font_map.items():
        print(f"  🔍 Validating: {name} ...", end=" ", flush=True)
        if validate_google_font(name):
            print("✅")
            valid[name] = paths
        else:
            print("❌ (not found on Google Fonts)")
            invalid.append(name)
    return valid, invalid


# ---------------------------------------------------------------------------
# Phase 4: Generate & Inject into index.html
# ---------------------------------------------------------------------------

def build_google_fonts_url(fonts: List[str], weights: List[int], display: str = "swap") -> str:
    """Build a Google Fonts CSS2 URL."""
    weight_str = ";".join(str(w) for w in sorted(weights))
    families = "&".join(
        f"family={name.replace(' ', '+')}:wght@{weight_str}"
        for name in sorted(fonts)
    )
    return f"https://fonts.googleapis.com/css2?{families}&display={display}"


def build_injection_block(fonts: List[str], weights: List[int], display: str = "swap") -> str:
    """Build the full HTML block to inject."""
    url = build_google_fonts_url(fonts, weights, display)
    lines = [
        INJECTION_MARKER_START,
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        f'<link href="{url}" rel="stylesheet">',
        INJECTION_MARKER_END,
    ]
    return "\n".join(lines)


def inject_into_html(index_path: Path, injection_block: str, dry_run: bool = False) -> bool:
    """Inject or replace the Google Fonts block in index.html."""
    if not index_path.is_file():
        print(f"⚠️  index.html not found: {index_path}")
        return False

    content = index_path.read_text(encoding="utf-8")

    # Check if already injected — replace
    start_idx = content.find(INJECTION_MARKER_START)
    end_idx = content.find(INJECTION_MARKER_END)

    if start_idx != -1 and end_idx != -1:
        end_idx += len(INJECTION_MARKER_END)
        new_content = content[:start_idx] + injection_block + content[end_idx:]
        action = "Replaced existing"
    else:
        # Insert before </head>
        head_close = content.find("</head>")
        if head_close == -1:
            print("⚠️  No </head> tag found in index.html")
            return False
        indent = "    "
        indented_block = "\n".join(indent + line for line in injection_block.split("\n"))
        new_content = content[:head_close] + indented_block + "\n" + content[head_close:]
        action = "Injected new"

    if dry_run:
        print(f"\n  📝 [DRY RUN] Would {action.lower()} Google Fonts block in {index_path}")
        print(f"  📝 [DRY RUN] Injection block:\n")
        for line in injection_block.split("\n"):
            print(f"      {line}")
        return True

    # Backup
    backup_path = index_path.with_suffix(".html.bak")
    shutil.copy2(index_path, backup_path)
    print(f"  💾 Backup saved: {backup_path}")

    index_path.write_text(new_content, encoding="utf-8")
    print(f"  ✅ {action} Google Fonts block in {index_path}")
    return True


# ---------------------------------------------------------------------------
# Phase 5: Font Class Optimization
# ---------------------------------------------------------------------------

def count_font_usage(font_map: Dict[str, List[str]]) -> Counter:
    """Count total occurrences of each font across all files."""
    counter = Counter()
    for name, paths in font_map.items():
        counter[name] = len(paths)
    return counter


def find_root_css(project_root: Path, explicit: Optional[str] = None) -> Optional[Path]:
    """Find the root CSS file to inject body font-family."""
    if explicit:
        p = project_root / explicit
        return p if p.is_file() else None

    for candidate in ROOT_CSS_CANDIDATES:
        p = project_root / candidate
        if p.is_file():
            return p
    return None


def add_root_font_family(css_path: Path, font_name: str, dry_run: bool = False) -> bool:
    """Add font-family to body in the root CSS file."""
    content = css_path.read_text(encoding="utf-8")

    rule = f"  font-family: '{font_name}', sans-serif;"

    # Check if body rule already exists
    body_match = re.search(r'(body\s*\{[^}]*)\}', content, re.DOTALL)
    if body_match:
        body_block = body_match.group(1)
        # Check if font-family already declared in body
        if "font-family" in body_block:
            if dry_run:
                print(f"  📝 [DRY RUN] body already has font-family in {css_path}, would update it")
            else:
                # Replace existing font-family in body
                updated_block = re.sub(
                    r'font-family\s*:[^;]+;',
                    f"font-family: '{font_name}', sans-serif;",
                    body_block
                )
                content = content.replace(body_block, updated_block)
                css_path.write_text(content, encoding="utf-8")
                print(f"  ✅ Updated body font-family to '{font_name}' in {css_path}")
            return True
        else:
            if dry_run:
                print(f"  📝 [DRY RUN] Would add font-family: '{font_name}' to body in {css_path}")
            else:
                # Add font-family to existing body block
                updated_block = body_block + f"\n{rule}\n"
                content = content.replace(body_block, updated_block)
                css_path.write_text(content, encoding="utf-8")
                print(f"  ✅ Added font-family: '{font_name}' to body in {css_path}")
            return True
    else:
        # No body rule — append one
        new_rule = f"\nbody {{\n{rule}\n}}\n"
        if dry_run:
            print(f"  📝 [DRY RUN] Would append body {{ font-family: '{font_name}' }} to {css_path}")
        else:
            content += new_rule
            css_path.write_text(content, encoding="utf-8")
            print(f"  ✅ Appended body font-family rule to {css_path}")
        return True


def remove_redundant_font_classes(
    project_root: Path,
    scan_dir: str,
    font_name: str,
    dry_run: bool = False
) -> int:
    """
    Remove font-['FontName'] classes from all files where font_name is the root font.
    Returns the number of removals.
    """
    target = project_root / scan_dir
    if not target.is_dir():
        return 0

    # Build patterns for this specific font
    # e.g. font-['Inter'], font-["Inter"], font-['Noto_Sans_SC'] (with underscore)
    underscore_name = font_name.replace(" ", "_")
    escaped_names = [re.escape(font_name)]
    if underscore_name != font_name:
        escaped_names.append(re.escape(underscore_name))

    # Match the full class token including surrounding whitespace context
    patterns = []
    for ename in escaped_names:
        # Match font-['Name'] or font-["Name"] with optional surrounding spaces in class strings
        patterns.append(re.compile(
            r"""\s*font-\[['"]""" + ename + r"""['"]\]"""
        ))

    total_removals = 0
    modified_files = []

    for root, _dirs, files in os.walk(target):
        rel_root = os.path.relpath(root, project_root)
        if any(skip in rel_root.split(os.sep) for skip in ["node_modules", "dist", ".git", ".output", ".nuxt"]):
            continue

        for fname in files:
            fpath = Path(root) / fname
            if fpath.suffix.lower() not in SCAN_EXTENSIONS:
                continue

            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            new_content = content
            file_removals = 0
            for pattern in patterns:
                matches = pattern.findall(new_content)
                file_removals += len(matches)
                new_content = pattern.sub("", new_content)

            # Clean up whitespace inside class attributes
            def clean_class_attr(match):
                content = match.group(1)
                content = re.sub(r'\s{2,}', ' ', content)  # collapse multiple spaces
                content = content.strip()  # trim leading/trailing
                return content

            new_content = re.sub(
                r'class="([^"]*?)"',
                lambda m: f'class="{clean_class_attr(m)}"',
                new_content
            )
            new_content = re.sub(
                r"class='([^']*?)'",
                lambda m: f"class='{clean_class_attr(m)}'",
                new_content
            )
            # Remove empty class attributes entirely
            new_content = re.sub(r'\s*class="\s*"', '', new_content)
            new_content = re.sub(r"\s*class='\s*'", '', new_content)

            if file_removals > 0:
                total_removals += file_removals
                rel_path = str(fpath.relative_to(project_root))
                modified_files.append((rel_path, file_removals))

                if not dry_run:
                    fpath.write_text(new_content, encoding="utf-8")

    if modified_files:
        prefix = "[DRY RUN] Would remove" if dry_run else "Removed"
        print(f"\n  🧹 {prefix} {total_removals} redundant font-['{font_name}'] classes:")
        for fpath, count in sorted(modified_files):
            print(f"      - {fpath}: {count} removal(s)")

    return total_removals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scan a Vue+Vite project for font declarations, validate & inject Google Fonts, optimize redundant classes."
    )
    parser.add_argument("project_root", help="Path to the project root directory")
    parser.add_argument("--no-optimize", action="store_true", help="Skip font class optimization (Phase 5)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--weights", default="300,400,700", help="Comma-separated font weights (default: 300,400,700)")
    parser.add_argument("--scan-dir", default="src", help="Directory to scan, relative to project root (default: src)")
    parser.add_argument("--index", default="index.html", help="Path to index.html, relative to project root")
    parser.add_argument("--root-css", default=None, help="Path to root CSS file for body font-family (auto-detect if omitted)")
    parser.add_argument("--display", default="swap", help="Google Fonts display parameter (default: swap)")
    parser.add_argument("--skip-validation", action="store_true", help="Skip Google Fonts validation (trust all non-system fonts)")

    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    if not project_root.is_dir():
        print(f"❌ Project root not found: {project_root}")
        sys.exit(1)

    weights = [int(w.strip()) for w in args.weights.split(",")]
    index_path = project_root / args.index

    print(f"🚀 Google Fonts Injector")
    print(f"   Project: {project_root}")
    print(f"   Scan dir: {args.scan_dir}")
    print(f"   Weights: {weights}")
    if args.dry_run:
        print(f"   Mode: DRY RUN (no files will be modified)")
    print()

    # Phase 1: Scan
    print("📁 Phase 1: Scanning for font declarations...")
    font_map = scan_fonts(project_root, args.scan_dir)
    if not font_map:
        print("  ℹ️  No font-['...'] declarations found. Nothing to do.")
        sys.exit(0)

    print(f"  Found {len(font_map)} unique font(s):")
    for name, paths in sorted(font_map.items()):
        print(f"    - {name} ({len(paths)} occurrence(s))")
    print()

    # Phase 2: Filter
    print("🔧 Phase 2: Filtering system fonts...")
    filtered = filter_system_fonts(font_map)
    removed = set(font_map.keys()) - set(filtered.keys())
    if removed:
        print(f"  Filtered out {len(removed)} system font(s): {', '.join(sorted(removed))}")
    else:
        print("  No system fonts to filter.")

    if not filtered:
        print("  ℹ️  No fonts remaining after filtering. Nothing to inject.")
        sys.exit(0)
    print()

    # Phase 3: Validate
    if args.skip_validation:
        print("🌐 Phase 3: Skipping validation (--skip-validation)")
        valid_fonts = filtered
        invalid_fonts = []
    else:
        print("🌐 Phase 3: Validating against Google Fonts...")
        valid_fonts, invalid_fonts = validate_fonts(filtered)

        if invalid_fonts:
            print(f"\n  ⚠️  {len(invalid_fonts)} font(s) not found on Google Fonts: {', '.join(invalid_fonts)}")

        if not valid_fonts:
            print("  ❌ No valid Google Fonts found. Nothing to inject.")
            print("     (If you're behind a firewall, try --skip-validation)")
            sys.exit(0)
    print()

    # Phase 4: Inject
    print("💉 Phase 4: Injecting into index.html...")
    font_names = sorted(valid_fonts.keys())
    block = build_injection_block(font_names, weights, args.display)
    inject_into_html(index_path, block, dry_run=args.dry_run)
    print()

    # Phase 5: Optimize
    if not args.no_optimize:
        print("🧹 Phase 5: Optimizing redundant font classes...")

        # Find the most-used font (only among valid Google Fonts)
        usage = count_font_usage(valid_fonts)
        most_common_font, most_common_count = usage.most_common(1)[0]
        print(f"  Most common font: {most_common_font} ({most_common_count} occurrence(s))")

        # Add to root CSS
        root_css = find_root_css(project_root, args.root_css)
        if root_css:
            print(f"  Root CSS file: {root_css.relative_to(project_root)}")
            add_root_font_family(root_css, most_common_font, dry_run=args.dry_run)
        else:
            print("  ⚠️  No root CSS file found. Skipping body font-family injection.")
            print("     You may want to manually add: body { font-family: '" + most_common_font + "', sans-serif; }")

        # Remove redundant classes
        remove_redundant_font_classes(project_root, args.scan_dir, most_common_font, dry_run=args.dry_run)
        print()

    # Summary
    print("=" * 60)
    print("📊 Summary")
    print("=" * 60)
    print(f"  Fonts injected into index.html: {', '.join(font_names)}")
    print(f"  Weights: {', '.join(str(w) for w in weights)}")
    if invalid_fonts:
        print(f"  Fonts NOT on Google Fonts (skipped): {', '.join(invalid_fonts)}")
    if not args.no_optimize:
        print(f"  Root font set to: {most_common_font}")
    print(f"  Google Fonts URL:")
    print(f"    {build_google_fonts_url(font_names, weights, args.display)}")
    print()
    print("✅ Done!" + (" (dry run — no files were modified)" if args.dry_run else ""))


if __name__ == "__main__":
    main()
