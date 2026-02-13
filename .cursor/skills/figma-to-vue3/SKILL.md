---
name: figma-html-cleanup-v2
description: >
  专为“等比例缩放”方案优化的 Figma HTML 清理工具。
  核心逻辑：清理 w-1920、提取全局导航/页脚、重算高度、图片重命名。
---

# Figma HTML 简洁清理转换 (等比例缩放版)

针对已实现整体等比例缩放的项目，对 Figma 导出的原始代码进行规范化清理。

---

## 1. 预处理：页面名称与目录
- **确定页面名**：从文件名提取（如 `about.html` -> `about`），非英文名根据内容生成（kebab-case）。
- **创建路由页面**：在 `src/pages/{页面名}/index.vue` 创建文件。

## 2. 代码转换流程（按顺序执行）

### 步骤 1 · 基础清理与定位修正
- **删除 w-1920**：移除所有元素上的 `w-1920` class。
- **保留 Absolute 布局**：不要强行转换 Flex。确保父容器（最外层 div）具备 `relative` 类。

### 步骤 2 · 提取 Navbar 和 Footer
- **识别**：根据位置（Top-0 或 Bottom-0）和内容（Logo, 版权信息）识别导航栏和页脚。
- **剥离**：将它们提取为 `@/components/layout/NavBar.vue` 和 `FooterBar.vue`。
- **全局管理**：在 `App.vue` 中引入并包裹 `<router-view>`，主页面代码中删除这部分 HTML。
- **记录高度**：记录两者的 `h-xx`（如 `h-100` 和 `h-402`）。

### 步骤 3 · 高度修正 (适应等比例缩放)
- **固定改最小**：将最外层容器的 `h-xx` 改为 `min-h-xx`。
- **高度重算**：`新 min-h = 原始总高度 - Footer高度`（Navbar 通常是 fixed/absolute 覆盖，不占用文档流空间，只需减去占位的 Footer 高度）。

### 步骤 4 · 图片本地化与重命名
- **扫描**：找出所有远程图片 URL。
- **重命名规则**：`[页面名或组件名]-[8位随机字符].[原扩展名]`。
  - 主页面：`home-a3f5b2c1.png`
  - NavBar：`navbar-x9k2m4n7.png`
- **保存路径**：主页面图存入 `@/assets/images/{页面名}/`，组件图存入 `@/assets/images/layout/`。
- **路径替换**：代码中统一改为 `@/assets/images/...`。

## 3. 输出清单
1. `src/pages/{页面名}/index.vue`（纯净的内容区块代码）。
2. `NavBar.vue` 和 `FooterBar.vue`（如果之前未生成）。
3. `App.vue` 引入代码示例。
4. **图片下载对照表**（远程 URL -> 本地路径）。
