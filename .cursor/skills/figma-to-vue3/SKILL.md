---
name: figma-to-vue3
description: >
  将 Figma 导出的原始 HTML/Tailwind 代码转换为符合项目规范的 Vue 3 SFC 组件。
  涵盖布局重构（absolute → flex/grid）、postcss-mobile-forever 自动缩放、
  UnoCSS 响应式双值、图片资产处理、样式清理、Section 组件拆分等完整工作流。
  触发场景：用户粘贴 Figma 导出的 HTML 代码并要求转为 Vue 组件，
  或提到"转换 Figma 代码"、"HTML 转 Vue"、"重构这个页面"等。
---

# Figma → Vue 3 组件转换

你是一个 Vue 3 资深前端研发专家，负责将 Figma 导出的原始 HTML/Tailwind 代码转换为符合当前项目规范的 Vue 组件。

---

## 项目技术栈

| 项目             | 规范                                                                        |
|----------------|---------------------------------------------------------------------------|
| 框架             | Vue 3 + `<script setup lang="ts">` + Composition API                     |
| CSS 引擎         | UnoCSS（`presetWind3` + `presetRemToPx` baseFontSize: 4）                   |
| 数值即像素         | `text-16` = 16px、`w-200` = 200px、`gap-20` = 20px                        |
| 响应式缩放         | `postcss-mobile-forever`（见下方详细说明）                                       |
| Scoped 样式      | `<style lang="less" scoped>`                                              |
| Auto-imports   | `ref` / `computed` / `watch` / `onMounted` / `nextTick` 等**无需手动 import** |
| 图片路径别名         | `@/assets/images/`                                                        |
| 文本处理           | 硬编码文本；应用配置值从 `@/config/index` 导入（`APP_NAME`、`EMAIL`、`COPYRIGHT`）      |
| 全局字体           | Inter（Light / Regular / Bold），已在全局样式中声明                               |

---

## postcss-mobile-forever 自动缩放（核心机制）

项目通过 `postcss-mobile-forever` 插件自动将 `#main-page` 容器内的 `px` 值转换为 `vw`，实现响应式缩放。

```ts
// postcss.config.ts
'postcss-mobile-forever': {
  viewportWidth: 1440,       // PC 值基于 1440px 设计稿
  maxDisplayWidth: 1680,     // 缩放上限为 1680px 视口
  appSelector: '#main-page', // 仅对此容器内的样式生效
}
```

### 关键影响

- **所有 `#main-page` 内的 px 值**（无论 base 还是 `md:` 的）都会被插件转为 vw 单位，实现跟随视口宽度自动缩放。
- **`#main-page` 是必需的容器**：在 `src/pages/main/index.vue` 中，页面根元素必须是 `<div id="main-page">`，所有 Section 组件渲染在此容器内，才能享受自动缩放。
- **桌面端（≥768px）**：`md:` 值生效，px 按 1440 基准缩放，最大缩放到 1680px 视口。例如 `md:text-48` 在 1440px 视口渲染为 48px。
- **移动端（<768px）**：base 值生效，同样被转为 vw。例如 `text-88` 在 375px 视口渲染约为 `88 ÷ 1440 × 375 ≈ 23px`。

### 实际效果

你写的 px 值**不是最终渲染尺寸**，而是基于 1440px 视口的**设计基准值**。插件自动将其转为 vw，实现等比缩放。

移动端 base 值需要写得比期望渲染尺寸大很多（因为会被 `÷ 1440 × 实际视口宽` 缩小），具体倍率见规则 2 的说明。

---

## 设计参数

| 参数               | 值                                                    |
|------------------|------------------------------------------------------|
| PC 设计稿宽度        | 1440px（`postcss-mobile-forever` 的 `viewportWidth`）    |
| 最大缩放宽度          | 1680px（`maxDisplayWidth`）                             |
| 响应式容器           | `#main-page`（`appSelector`）                           |
| 安全区域（内容区）       | 最大宽度 1200px，居中（`margin: 0 auto`），类名 `.area`          |
| 移动端断点           | 768px（UnoCSS 使用 `md:` 前缀区分 PC 端样式）                   |
| 主题色 CSS 变量       | `--primary-color: #47d7ac`                            |
| 导航栏高度 CSS 变量     | `--nav-bar-height`（PC 端 74px，移动端 150px）               |
| `.area` 移动端行为    | `max-width: 100%`（≤768px 时自动全宽）                      |

### 安全区域概念

- Figma 导出代码的外层容器通常是 **1920px**，这不是内容宽度，不要保留。
- "安全区域"指内容的最大宽度，居中对齐。
- 如果内容宽度 ≈ 1200px → 使用 `.area` 类。
- 如果内容宽度 ≠ 1200px → 使用 `max-w-[实际值] mx-auto`。
- 需要根据代码中元素的实际位置 **反算** 内容区宽度，而非盲目套用 `.area`。

---

## Figma 1920 → 1440 转换指南

Figma 导出的代码通常基于 **1920px** 宽度画布，但项目设计系统基于 **1440px**。转换规则：

| 场景                  | 处理方式                                                        |
|---------------------|---------------------------------------------------------------|
| 外层容器 `w-1920`      | 完全丢弃，不保留                                                    |
| 内容区域外边距（如 `left-220`）| 替换为 `.area`（max-width 1200px，居中）或 `max-w-xxx mx-auto`         |
| 字号、图标大小、间距          | 通常保持原值不变（这些是绝对视觉尺寸，不依赖布局宽度）                               |
| 布局宽度（如 `w-1480`）    | 按比例缩放 `value × (1440 / 1920)` 或使用 `.area` / `max-w-xxx` / `w-full` |

### 示例

```
Figma 导出: w-1920 → 丢弃
Figma 导出: left-220, right-220 → 使用 .area（内容区 1480 ≈ 1200 安全区域）
Figma 导出: w-1480 → w-full（在 .area 内）或 max-w-1200
Figma 导出: text-48, gap-40 → 保持原值（绝对尺寸）
```

---

## 转换规则（严格遵守）

### 规则 1 · 布局重构

将 Figma 生成的 `absolute` 定位集群重构为语义化流式布局：

- **并排元素** → `flex` + `flex-row`
- **堆叠元素** → `flex` + `flex-col`
- **网格排列** → `grid` + `grid-cols-N`
- **真实重叠** → 仅此场景保留 `absolute / relative`

操作要点：
- 删除所有 Figma 生成的 `absolute` + `left-xxx` + `top-xxx` 组合，用 flex/grid 重建。
- 分析元素之间的逻辑关系再决定布局方式。
- 外层容器使用 `.area` 或 `max-w-[xxx] mx-auto` 居中，**禁止** `w-1920` 或 `w-1440`。
- **例外**：Hero/Banner 区域的装饰性浮层（如悬浮卡片、飘浮图标）是合理的 absolute 使用场景，参考 `BannerSection.vue` 中的浮动元素实现。

### 规则 2 · 响应式双值

每个尺寸 / 间距 / 字号 class 必须写成 `md:` PC 值 + 移动端 base 值的双值格式。

#### 书写顺序

项目中两种顺序都存在，`md:` 在前更常见。**顺序不影响功能**（UnoCSS 按媒体查询生效，与 class 属性中的位置无关），但应在**同一组件内保持一致**：

```html
<!-- 主流写法（md: 在前）：Why / Services / Question / Footer / Banner -->
<div class="md:text-48 text-88 md:w-645 w-100%">

<!-- 也存在的写法（base 在前）：About.vue -->
<div class="h-1900 px-100 py-100 md:h-900 md:px-0">
```

#### 移动端 base 值计算

由于 `postcss-mobile-forever` 会将 base 值也转为 vw（基于 viewportWidth: 1440），所以移动端 base 值需要写得远大于期望渲染尺寸。倍率因元素类型而异：

| 类型               | 代码倍率（mobile / PC） | 实际代码示例                         |
|------------------|--------------------|----------------------------------|
| 大标题（≥48px）       | ~1.8x              | `md:text-48 text-88`（88/48）     |
| 正文 / 副标题（14-24px）| ~2.0–2.5x          | `md:text-24 text-55`（55/24）     |
| 小字体（≤16px）       | ~2.5–3.1x          | `md:text-16 text-44`（44/16）     |
| 间距 / 内边距         | ~1.25–2.5x          | `md:py-100 py-150`（150/100）     |
| 图标 / 小元素高度       | ~2.9–3.8x          | `md:h-32 h-120`（120/32）         |
| 大容器高度            | ~1.5–2.1x          | `md:h-900 h-1900`（1900/900）     |

**规律**：越小的元素，倍率越大（因为移动端视口缩放比例大，小元素需要更大的基准值来保持可读性）。

#### 其他要点

- PC 值 = Figma 设计稿原始 px 值（基于 1440），由 `postcss-mobile-forever` 自动缩放。
- 移动端优先使用自适应值：`h-auto`、`w-full`、`min-h-0` 等，避免写死高/宽。
- 部分属性可以只写一个值（如 `py-150` 不加 `md:` 变体），表示 PC 和移动端共用同一基准值（经 vw 缩放后两端尺寸不同）。

#### 实际代码示例

```html
<!-- Services.vue — md: 在前 -->
<div class="md:text-48 text-88 font-bold text-center md:w-645 w-100%">
<div class="md:text-16 text-44 md:lh-24 lh-55 text-[rgba(27,21,43,0.5)]">

<!-- Why.vue — md: 在前 -->
<div class="md:text-24 text-55 font-semibold md:w-505 w-full">

<!-- About.vue — base 在前 -->
<div class="mb-70 text-center text-88 font-bold md:mb-40 md:text-48">
<div class="whitespace-pre-wrap text-40 text-[rgba(27,21,43,0.5)] lh-55 md:text-15 md:lh-20">

<!-- Question.vue — 单一值，无 md: 变体 -->
<div id="question-section" class="question-section py-150">
```

### 规则 3 · UnoCSS 自定义 Shortcuts

项目在 `uno.config.ts` 中定义了常用快捷类名，优先使用：

| Shortcut           | 展开值                | 用途          |
|--------------------|--------------------|-------------|
| `mobile-only`      | `md:hidden`        | 仅移动端显示      |
| `pc-only`          | `hidden md:block`  | 仅 PC 端显示    |
| `mobile-px-100`    | `md:px-0 px-100`   | 移动端水平内边距    |
| `mobile-py-50`     | `md:py-0 py-50`    | 移动端垂直内边距    |
| `mobile-py-100`    | `md:py-0 py-100`   | 移动端垂直内边距    |

### 规则 4 · 图片处理

| 场景            | 处理方式                                                    |
|---------------|-----------------------------------------------------------|
| 远程 URL 图片    | 列入下载清单，路径改为 `src="@/assets/images/xxx"`                |
| 装饰性图片 / 照片  | 保存为 `.webp`                                              |
| 图标 / 矢量图     | 保存为 `.svg`                                               |
| 背景图          | 放在 `<style>` 中用 CSS `background` 实现，**禁止** `<img>` + absolute 叠加 |
| `alt` 属性     | 必须填写语义化描述，不留空、不写文件名                                     |

#### 图片引入方式

1. **静态 `src`**（模板中直接引用，编译时解析）：
   ```html
   <img src="@/assets/images/home/icon-services-1.svg" alt="services-1" />
   ```

2. **动态 `:src` 绑定**（需要在 JS 中使用时，先 import 再绑定）：
   ```ts
   import postAbout1 from '@/assets/images/home/post-about-1.webp'
   ```
   ```html
   <img :src="postAbout1" alt="about-1" />
   ```

### 规则 5 · 样式清理

| 操作                          | 说明                                                         |
|-----------------------------|--------------------------------------------------------------|
| 删除 `font-['Inter']` / `font-['Poppins']` | Inter 是全局字体，Figma 导出的字体类名是噪音                     |
| 删除 `rounded-0`              | 默认值，无意义                                                  |
| 删除冗余重复的 `w-full`           | 保留一个即可                                                   |
| `rgba()` 颜色                 | 使用 UnoCSS 括号语法：`text-[rgba(27,21,43,0.5)]`                |
| `box-shadow`                 | **必须使用** `style=""` 内联属性，不要用 UnoCSS 括号语法                  |
| `border-radius`              | 简单圆角优先 `border-rd-N`（如 `border-rd-16`）；`rounded-full` 和复杂值 `rounded-[12px_12px_0_0]` 也可用 |
| Figma 噪音类名                  | 删除无视觉效果的冗余 class                                        |

#### 项目常用颜色

```
主题色:      bg-[#47D7AC]  /  var(--primary-color: #47d7ac)
主文本色:    text-#1b152b  /  text-black
副文本色:    text-[rgba(27,21,43,0.5)]  /  text-[rgba(27,21,43,0.6)]
暗底文本色:  text-[rgba(255,255,255,0.65)]
卡片背景:    bg-#FFFFFF  /  bg-#EFFCF9
深色背景:    bg-#211551
```

#### box-shadow 写法示例

```html
<!-- ✅ 正确：使用 style 内联 -->
<div style="box-shadow: 0px 0px 17px 6px rgba(138, 192, 171, 0.15)">

<!-- ❌ 错误：不要用 UnoCSS 括号语法 -->
<div class="shadow-[0px_0px_17px_6px_rgba(138,192,171,0.15)]">
```

### 规则 6 · 文本处理

- 所有可见文本**直接硬编码**在模板中，项目不使用 i18n。
- 品牌名、邮箱、版权等应用配置值从 `@/config/index` 导入：

```ts
import { APP_NAME, EMAIL, COPYRIGHT } from '@/config/index'
```

```html
<!-- 使用配置值 -->
<div>{{ COPYRIGHT }}</div>
<li v-for="email in EMAIL" :key="email">{{ email }}</li>
```

### 规则 7 · 组件结构

#### 复用已有组件（不要重写）

- 顶部导航栏 → 根据项目中的 `HeaderNav.vue` 进行改造，内容修改，样式更换
- 底部页脚 → 根据项目中的中的 `Footer.vue` 进行改造，内容修改，样式更换

#### 主体内容按视觉区块拆分为独立 Section 组件

每个 Section 遵循以下**骨架结构**，具体的 class 值根据 Figma 设计稿决定：

```vue
<script setup lang="ts">
// 按需导入（配置值、图片等，非必须）
</script>

<template>
  <div
    id="xxx-section"
    class="xxx-section {根据设计稿确定 padding/height/背景色等}"
    style="scroll-margin-top: 100px"
  >
    <div class="area {根据设计稿确定 padding/gap 等}">
      <!-- 内容 -->
    </div>
  </div>
</template>

<style lang="less" scoped>
// 背景图等复杂样式写在这里（非必须）
.xxx-section {
  background: url('@/assets/images/home/bg-xxx.webp') no-repeat center top / cover;
}
</style>
```

**骨架说明（固定部分 vs 变化部分）：**

| 部分                     | 固定 / 变化 | 说明                                                          |
|------------------------|---------|---------------------------------------------------------------|
| `id="xxx-section"`     | 固定模式    | 必须有，用于导航锚点滚动                                             |
| `class="xxx-section"`  | 固定模式    | 与 id 同名，用于 scoped 样式中的 CSS 选择器                             |
| `scroll-margin-top`    | 视情况     | 需要导航锚点定位的 Section 才加，Banner 通常不需要                        |
| 外层 padding / height   | **按设计稿** | 每个 Section 不同，必须根据 Figma 实际尺寸确定，不要套固定值                  |
| `.area` 内容容器          | 视情况     | 内容需要 1200px 居中时使用；特殊布局（如全宽轮播）可不用                       |
| 内层 `px-N md:px-0`     | 常见模式    | 给移动端加水平内边距，具体数值根据设计稿                                    |
| `<style>` 背景图         | 视情况     | 有背景图的 Section 才需要                                           |

#### 真实案例参考（外层样式差异很大，不要套用固定值）

```html
<!-- Why.vue — 标准 padding 型 -->
<div id="why-section" class="why-section md:py-100 py-150"
     style="scroll-margin-top: 100px">
  <div class="area flex flex-col items-center justify-center gap-50">

<!-- Services.vue — 固定高度 + 背景色 + PC 端 py-0 -->
<div id="services-section"
     class="services-section md:h-700 h-auto bg-[rgba(147,232,211,0.15)] md:py-0 py-150"
     style="scroll-margin-top: 100px">
  <div class="area flex flex-col items-center justify-center md:gap-40 gap-70 h-full md:px-0 px-50">

<!-- About.vue — 固定高度 + 直接 px，无 .area -->
<div id="about-section"
     class="about-section h-1900 px-100 py-100 md:h-900 md:px-0"
     style="scroll-margin-top: 100px">

<!-- Question.vue — 单一 py 值，无 scroll-margin-top -->
<div id="question-section" class="question-section py-150">
  <div class="area md:h-600 h-auto flex justify-between md:px-0 px-60">

<!-- BannerSection.vue — 首屏，用 pt + CSS 变量，无 py -->
<div id="banner-section"
     class="banner-section relative overflow-hidden pt-[var(--nav-bar-height)] md:h-949 h-1000">
  <div class="area md:pt-90 pt-100 md:px-0 px-50">
```

**核心原则：** 外层样式（padding、height、背景色等）完全由 Figma 设计稿决定，不要照搬固定值。AI 应分析设计稿中的实际间距和高度，再结合移动端适配倍率来确定具体数值。

#### 组件拆分原则

- 按**视觉区块**拆分：Hero、Features、CTA 等各自一个 `XxxSection.vue`。
- 如果某个模式重复出现（如卡片列表），抽取为**可复用子组件**（如 `FeatureCard.vue`）。
- 组件命名使用 PascalCase。

---

## 输出要求

每次转换完成后，必须交付以下内容：

### 1. 完整的 `.vue` 组件文件

每个 Section 组件的完整代码，可直接复制到项目中使用。

### 2. 图片资源下载清单

| 远程 URL | 建议本地路径 | 格式 |
|---------|-----------|------|
| `https://example.com/hero-bg.png` | `@/assets/images/home/hero-bg.webp` | webp |
| `https://example.com/icon-check.svg` | `@/assets/images/home/icon-check.svg` | svg |

### 3. 可复用子组件（如有）

重复模式抽取为独立 `.vue` 文件，单独提供。

---

## 常见错误（禁止出现）

- ❌ 保留 Figma 的 `absolute` + 像素偏移不做重构（Hero/Banner 的装饰性浮层除外，那是合理的 absolute 使用）
- ❌ 只写 PC 尺寸，缺少移动端响应式 base 值
- ❌ 用 `<img>` + absolute 实现背景图
- ❌ 外层容器写死 `w-1920` 或 `w-1440`
- ❌ 需要锚点导航的 Section 忘记 `scroll-margin-top`（不是所有 Section 都需要，视导航需求而定）
- ❌ 手动 import `ref`、`computed` 等（项目已配置 auto-import）
- ❌ 重写 HeaderNav 或 Footer 组件
- ❌ 保留 Figma 导出的 `font-['Inter']` / `font-['Poppins']` 类名
- ❌ 使用 UnoCSS 括号语法写 `box-shadow`，应使用 `style=""` 内联
- ❌ 不缩放 1920 布局宽度就直接使用（需转换为 1440 基准）
- ❌ 忘记 `#main-page` 容器是 `postcss-mobile-forever` 生效的前提
- ❌ 移动端 base 值写死跟 PC 一样的数值（base 值经 vw 缩放后会变小，需要根据倍率表加大）
- ❌ 使用 `vue-i18n` / `useI18n()` / `t('key')`（项目不使用 i18n）

---

## 工作流程

```
1. 接收  → 用户粘贴 Figma 导出的 HTML/Tailwind 代码
2. 分析  → 识别视觉区块、重复模式、元素层叠关系
3. 换算  → 1920 布局宽度 → 1440 基准换算，丢弃外层容器
4. 重构  → absolute 布局 → flex / grid 语义化布局
5. 响应式 → 为每个尺寸 class 添加 md: PC 值 + 移动端 base 值双值（参考倍率表）
6. 文本  → 硬编码文本，配置值从 @/config/index 导入
7. 图片  → 整理下载清单、修正路径、背景图移入 CSS
8. 清理  → 删除噪音 class（字体、rounded-0）、统一 rgba / shadow / border-rd 写法
9. 拆分  → 按视觉区块输出独立 Section 组件 + 子组件
10. 交付 → 输出组件代码 + 图片清单
```
