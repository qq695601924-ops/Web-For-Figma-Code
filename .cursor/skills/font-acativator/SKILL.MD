---
name: font-activator
description: |
  扫描 Vue + Vite SPA 项目中的 Tailwind/UnoCSS 字体声明（font-['xxx']），自动从 Google Fonts 引入并注入 index.html，同时优化 AI 生成代码中冗余的字体类。
  当用户提到以下任意场景时触发：字体没生效、font-['xxx'] 没加载、引入 Google Fonts、清理冗余字体类、字体优化、AI 生成代码字体太多重复。
---

# Font Activator

扫描项目字体声明 → 验证 Google Fonts → 注入 index.html → 优化冗余字体类。

## 适用场景

- 项目使用了 `font-['Inter']` 等类名但字体未加载
- AI 生成的代码在每个元素上都加了 `font-['xxx']`，需要清理
- 想根据代码实际使用情况自动引入 Google Fonts

## 执行流程

### 阶段 1：扫描
递归扫描 `src/` 下 `.vue/.tsx/.jsx/.html/.css` 文件，匹配 `font-['Inter']`、`font-["Roboto"]`、`font-['Noto_Sans_SC']` 等模式。

### 阶段 2：过滤
剔除系统字体（Arial、Helvetica、sans-serif、Microsoft YaHei、PingFang SC 等），只保留需要远程加载的。

### 阶段 3：验证
对每个字体向 `fonts.googleapis.com` 发 HEAD 请求，确认存在才保留。可用 `--skip-validation` 跳过（离线或网络受限时）。

### 阶段 4：注入
在 `index.html` 的 `</head>` 前插入 preconnect + stylesheet 链接，默认权重 300/400/700。重复运行会替换不会重复。

### 阶段 5：优化（默认开启）
1. 统计最高频字体
2. 将其写入根 CSS 的 `body { font-family }`
3. 从所有文件中移除该字体的冗余 `font-['xxx']` 类
4. 清理残留空格和空 class 属性

## 使用方式

```bash
python3 scripts/inject_google_fonts.py <项目根目录> [选项]
```

### 选项

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--dry-run` | false | 预览模式，不修改文件 |
| `--no-optimize` | false | 跳过阶段 5（字体类优化） |
| `--skip-validation` | false | 跳过 Google Fonts 验证 |
| `--weights` | `300,400,700` | 字体权重，逗号分隔 |
| `--scan-dir` | `src` | 扫描目录（相对项目根） |
| `--index` | `index.html` | index.html 路径（相对项目根） |
| `--root-css` | 自动检测 | 根 CSS 文件路径 |
| `--display` | `swap` | Google Fonts display 参数 |

## Agent 执行步骤

1. 定位项目根目录（包含 `index.html` 和 `src/` 的目录）
2. 先 dry-run 预览：
   ```bash
   python3 scripts/inject_google_fonts.py <项目根目录> --dry-run
   ```
3. 将结果展示给用户确认
4. 确认后正式执行：
   ```bash
   python3 scripts/inject_google_fonts.py <项目根目录>
   ```
5. 报告：注入了哪些字体、移除了多少冗余类

## 注意事项

- 脚本幂等，重复运行安全
- 下划线字体名（`Noto_Sans_SC`）自动转空格
- 修改前自动备份 `index.html` 为 `index.html.bak`
- 验证阶段需要网络；无网络时用 `--skip-validation`
- 优化只处理最高频字体，其余保留不动，避免破坏局部覆盖
