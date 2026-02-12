---
name: figma-html-cleanup
description: >
  清理 Figma 导出的 HTML/Tailwind 代码，执行固定的转换流程：
  预处理（确定页面名称和创建目录）、去除 w-1920、提取 navbar/footer 为独立组件、
  固定高度改最小高度、重算父容器最小高度、下载远程图片到本地。
  触发场景：用户上传 HTML 文件、提供 HTML 代码片段，并要求清理或转换。
---

# Figma HTML 清理转换

对 Figma 导出的原始 HTML/Tailwind 代码执行完整的转换流程，包括预处理和 5 个代码转换步骤。

---

## 工作流程

### 输入处理

用户可能提供以下三种输入方式：

1. **单个 HTML 文件**：上传一个 `.html` 文件
2. **多个 HTML 文件**：上传多个 `.html` 文件
3. **HTML 代码片段**：直接提供一段 HTML 代码

### 页面创建规则

**重要**：本技能会自动在 `src/pages` 目录下创建对应的路由页面。

#### 1. HTML 文件处理

- **提取文件名**：从 HTML 文件名中提取页面名称（去掉 `.html` 扩展名）
- **文件名处理**：
  - 如果文件名是英文（仅包含字母、数字、连字符、下划线），直接使用
  - 如果文件名不是英文（包含中文或其他非英文字符），根据 HTML 内容生成合适的英文文件夹名
    - 分析 HTML 内容（title、h1、主要文本等）
    - 生成语义化的英文名称（如：`home`、`about`、`contact`、`product-detail` 等）
    - 使用 kebab-case 命名风格（小写字母，单词间用连字符分隔）
- **创建目录结构**：在 `src/pages` 下创建对应的文件夹
  - 例如：`about.html` → `src/pages/about/index.vue`
  - 例如：`产品详情.html` → 根据内容生成如 `src/pages/product-detail/index.vue`

#### 2. HTML 代码片段处理

- 如果没有提供文件名，根据 HTML 内容生成英文文件夹名
- 分析 HTML 内容（title、h1、主要文本、class 名称等）来确定页面用途
- 创建对应的文件夹和 `index.vue` 文件

#### 3. 多个 HTML 文件处理

- **依次处理**：对每个 HTML 文件依次执行完整的转换流程（预处理 + 5 个代码转换步骤）
- **独立页面**：每个 HTML 文件对应一个独立的路由页面
- **共享组件**：navbar 和 footer 组件会被提取并共享（仅在首次或结构变化时创建）
- **处理顺序**：按照用户提供的文件顺序，逐个处理每个文件
- **组件复用**：第一个文件处理时会创建 navbar/footer 组件，后续文件会复用这些组件，只替换引用即可

---

## 完整执行流程

对于每个 HTML 输入（单个文件、代码片段或批量文件中的每一个），按以下顺序执行：

### 预处理 · 确定页面名称和创建目录

1. **确定页面名称**（根据文件名或内容生成）
   - HTML 文件：提取文件名（去掉 `.html` 扩展名）
   - 非英文文件名：根据 HTML 内容（title、h1、主要文本等）生成英文文件夹名
   - HTML 代码片段：根据内容生成英文文件夹名
   - 使用 kebab-case 命名风格

2. **创建页面目录**
   - 在 `src/pages` 下创建 `{页面名}/index.vue` 文件
   - 例如：`about.html` → `src/pages/about/index.vue`

> **注意**：项目使用 `unplugin-vue-router`，在 `src/pages` 目录下创建的文件会自动生成对应的路由。例如 `src/pages/about/index.vue` 会自动生成 `/about/` 路由。

**批量处理时**：完成第一个文件的全部流程后，再开始处理下一个文件。

---

## 代码转换步骤（按顺序执行）

> **步骤依赖关系**：
> - 步骤 1：基础清理，独立执行
> - 步骤 2：提取组件，为后续步骤提供高度信息
> - 步骤 3：依赖步骤 2（需要知道组件已提取）
> - 步骤 4：依赖步骤 2 和 3（需要组件高度和 min-h 值）
> - 步骤 5：依赖所有步骤（文件结构确定后才能准确替换图片路径）

---

### 步骤 1 · 去除 w-1920

- 删除父元素及所有元素上的 `w-1920` class。
- 如果父元素只有 `w-1920` 作为宽度约束，替换为 `w-full`。

> **目的**：移除固定宽度约束，使页面响应式。

---

### 步骤 2 · 提取 navbar 和 footer 为独立组件

将 navbar 和 footer 从主代码中**剥离**，各自输出为独立组件文件。

> **为什么先提取组件**：后续步骤需要用到 navbar 和 footer 的高度信息来计算主容器高度，所以需要先提取并识别它们的高度。

> **自动识别**：不依赖用户指定 id 或标注，AI 根据下方规则自动判断。如果判断不确定，在输出中标注理由让用户确认。

> **去重**：每次 Figma 复制的代码可能都包含 navbar 和 footer。如果之前已经生成过 `NavBar.vue` 和 `FooterBar.vue`，则**跳过生成**，只从主代码中移除对应部分并替换为组件引用即可。仅在首次出现或结构明显不同时才输出组件文件。

> **调整层级**：navbar 默认 fixed 到顶部，z-index 设为 199。

#### 识别规则（当没有明确 id 时）

**Navbar 判定**（满足 2 条以上即可认定）：
- 位于文档最顶部的第一个子元素
- 包含 `top-0` 或 `fixed` / `sticky`
- z-index 值最高
- 横向满宽（`w-full` / `w-1920`）
- 内容含 logo 图片 + 导航链接

**Footer 判定**（满足 2 条以上即可认定）：
- 位于文档最底部的最后一个子元素
- 内容含版权文字（©、Copyright）、社交图标、联系方式
- 横向满宽

#### 输出

- `NavBar.vue` → `@/components/layout/NavBar.vue`
- `FooterBar.vue` → `@/components/layout/FooterBar.vue`
- **主代码中移除 navbar/footer**：从主页面代码中完全删除 navbar 和 footer 的 HTML 代码，**不要**替换为组件引用
- **记录高度**：提取 navbar 和 footer 的高度值（从 `h-xx` class 中读取），用于后续步骤计算

> **重要**：如果输出了独立的组件文件，**必须在 App.vue 中引入并使用** NavBar 和 FooterBar 组件：
> - 在 App.vue 的 `<template>` 中，在 `<router-view>` 之前添加 `<NavBar />`，在 `<router-view>` 之后添加 `<FooterBar />`
> - 在 App.vue 的 `<script setup>` 中添加 `import NavBar from '@/components/layout/NavBar.vue'` 和 `import FooterBar from '@/components/layout/FooterBar.vue'`
> - **不要在各个页面文件中单独引入** NavBar 和 FooterBar，它们应该在 App.vue 中统一管理，这样所有页面都能共享这些布局组件

---

### 步骤 3 · 固定高度改最小高度

- 父元素（最外层容器）的 `h-xx` 改为 `min-h-xx`。
- 目的：允许内容撑开，避免移动端溢出。

> **执行时机**：在提取 navbar/footer 之后执行，因为下一步需要基于这个 min-h 值进行修正。

---

### 步骤 4 · 重算父容器 min-h

步骤 3 得到的 `min-h-xx` 值需要修正，因为 navbar 和 footer 已经从主容器中移除：

```
新 min-h = 原始 h 值 - footer 高度
```

- navbar 高度：从步骤 2 中提取的 navbar 元素的 `h-xx` class 中读取。
- footer 高度：同理。
- 如果无法确定具体高度，在代码中用注释标注 `/* TODO: 减去 footer 高度 */`。

> **为什么需要修正**：navbar 和 footer 已提取为独立组件，主容器的高度应该减去它们的高度，避免页面高度计算错误。

---

### 步骤 5 · 下载远程图片（最后执行）

> **执行时机**：在所有代码结构确定之后执行，因为步骤 2 会把 navbar/footer 拆成独立组件，图片所在文件会变化；在最终代码结构上统一收集并替换图片引用，路径更准确、也便于按页面或组件组织资源。

> **页面名来源**：本步骤中使用的"页面名"必须是**预处理步骤中确定的页面名**（从 HTML 文件名提取或根据内容生成的英文名称，如 `home`、`about`、`product-detail` 等）。如果预处理步骤确定的页面名是 `home`，则所有主页面图片都使用 `home-{随机值}.{扩展名}` 格式，无论图片 URL 中包含什么字符。

- **范围**：对**最终产出**的所有代码（主页面 + `NavBar.vue` + `FooterBar.vue`）一起扫描。
- 找出所有 `http://` 或 `https://` 开头的图片 URL（img src、background-image 等）。
- **图片重命名规则**：
  - Figma 提供的图片 URL 可能包含特殊字符（如冒号 `:`、URL 编码的 `%3A`、端口号等），这些字符在文件系统中可能不被支持
  - **重要**：页面名必须使用**预处理步骤中确定的页面名**（从文件名提取或根据内容生成的英文名称），**绝对禁止**从图片 URL 中提取任何部分作为页面名
  - **统一使用 `[页面名]-[随机值].[扩展名]` 格式重命名**
  - 主页面图片：`{页面名}-{随机8位字符}.{扩展名}`，例如：如果页面名是 `home`，则生成 `home-a3f5b2c1.png`
  - NavBar 组件图片：固定使用 `navbar-{随机8位字符}.{扩展名}`，例如：`navbar-x9k2m4n7.png`
  - FooterBar 组件图片：固定使用 `footer-{随机8位字符}.{扩展名}`，例如：`footer-p8q1r3s6.png`
  - 随机值使用 8 位十六进制字符（0-9a-f），确保唯一性
  - 保留原始图片格式（扩展名），不做格式转换
  - **禁止行为**：不要从 URL 路径、查询参数、端口号等任何部分提取文件名，URL 仅用于下载图片，文件名完全由页面名+随机值生成
- **输出下载清单**，格式如下（假设预处理步骤确定的页面名是 `home`）：

| 远程 URL | 本地路径 |
|---------|---------|
| `https://example.com/126%3A1961-Group.png` | `@/assets/images/home/home-a3f5b2c1.png` |
| `https://example.com/logo.png` | `@/assets/images/layout/navbar-x9k2m4n7.png` |

> **注意**：示例中的 `home` 是预处理步骤中确定的页面名，不是从 URL 中提取的。无论 URL 中包含什么字符（如 `126%3A1961`），都**不能**用作文件名的一部分。

- 可按所属文件区分资源目录（如主页面用 `页面名`，navbar/footer 用 `layout`），避免混在一起。
- 代码中的引用路径统一改为 `@/assets/images/...`。

---

## 输出清单

每次转换完成后交付：

1. **页面文件**：`src/pages/{页面名}/index.vue`（清理后的主页面代码，**不包含** navbar 和 footer）
2. **NavBar.vue** 独立组件（仅首次或结构变化时输出）→ `@/components/layout/NavBar.vue`
3. **FooterBar.vue** 独立组件（仅首次或结构变化时输出）→ `@/components/layout/FooterBar.vue`
4. **App.vue 更新**（如果创建了 NavBar 或 FooterBar 组件）：
   - 在 `<script setup>` 中引入组件
   - 在 `<template>` 中添加 `<NavBar />` 和 `<FooterBar />` 组件
5. **图片下载清单**（远程 URL → 本地路径 表格，使用重命名后的文件名）
6. **页面说明**：生成的页面名称和对应的路由路径

### 多个文件处理说明

当处理多个 HTML 文件时：
- 每个文件都会生成独立的页面和输出清单
- navbar 和 footer 组件只会在首次出现时创建，后续文件会复用这些组件
- **App.vue 更新**：只在首次创建 NavBar 或 FooterBar 组件时更新 App.vue，后续文件处理时不再重复更新
- 图片资源按页面分别组织到对应的 `@/assets/images/{页面名}/` 目录下
- 所有图片都使用 `[页面名称或组件名]-[随机值].[扩展名]` 格式重命名，避免特殊字符问题
