---
name: faq-accordion-refactor
description: >
  将原始生成的折叠/展开/手风琴面板代码改造为项目内的 FaqAccordion 组件。
  当原始输出的代码中包含手动实现的折叠面板（多个 div 切换显隐、FAQ 列表、
  帮助中心问答、手风琴效果）时触发此 skill。也适用于用户要求"用组件替换"、
  "改造成组件"、"接入 FaqAccordion"等场景。即使原始代码结构、样式各不相同，
  都应使用本 skill 统一改造。
---

# Generated Code → Project FaqAccordion Component Refactor

## 改造规则（必须遵守，严格执行，尤其是2和3）

1. **数据来源**：FAQ 列表统一从 `@/config/faq.ts` 导入，忽略原始代码中硬编码的 FAQ 文案内容。页面中不再内联任何 title/content 文本，仅做渲染消费。若原始代码中出现写死的 FAQ 问答文本，一律丢弃，不做提取，以 `faq.ts` 为唯一数据源。

2. **样式替换（很重要）**：先分析 AI 代码中 open 和 close 两种状态下的样式差异，然后仅迁移以下显示类样式，直接修改到 FaqAccordion 组件内部的 class / style，通过 :class 或 :style 绑定 `isOpen(index)` 状态区分展开/收起态。不通过 props、CSS 变量、外层容器覆盖。

- ✅ 迁移：标题字体大小、标题颜色、内容字体大小、内容颜色、面板背景颜色、面板圆角、关闭按钮大小
- ❌ 不替换：高度、宽度、间距、padding、margin 等布局类样式（会破坏组件展开收起的核心逻辑）
- ⚠️ 操作原则：只替换对应的样式值，不删除 FaqAccordion 组件中任何已有的 class。 例如需要改背景色，只替换 bg-xxx 为新值，其余 class 原样保留。

3. **图标处理（很重要）**：从原始代码中识别展开/收起图标资源路径，通常第一个图标为展开态，第二个为收起态。将图标路径更新到 FaqAccordion 组件内部对应的 `<img>` 标签中。

4. **输出格式**：页面中一行调用即可，不在外部使用 `v-for`，列表遍历已内置于组件中：

```vue
<script setup lang="ts">
import { faqList } from '@/config/faq'
</script>

<template>
  <!-- 手风琴模式：同时只展开一个，默认展开第一项 -->
  <FaqAccordion :list="faqList" accordion :default-open="0" />

  <!-- 独立模式：每项可独立展开/收起 -->
  <FaqAccordion :list="faqList" />
</template>
```

## FaqAccordion Props

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `list` | `FaqItem[]` | — (必传) | FAQ 数据列表 |
| `accordion` | `boolean` | `false` | 是否启用手风琴模式（互斥展开） |
| `defaultOpen` | `number` | `undefined` | 默认展开项的索引，不传则全部收起 |

## faq.ts 结构

```ts
export interface FaqItem {
  title: string
  content: string
}

export const faqList: FaqItem[] = [...]
```

若 `faq.ts` 尚不存在，提示用户先创建并给出上述模板。

## 禁止行为

- ❌ 不在页面中内联任何 FAQ 文案
- ❌ 不手动重写折叠展开逻辑
- ❌ 不在页面中使用 `v-for` 遍历列表（遍历已内置于 FaqAccordion 组件内部）
- ❌ 不在 `v-for` 外单独写死折叠项
- ❌ 不通过 props 或外层容器传递样式
- ❌ 不使用旧的 Collapse 单项组件，统一使用 FaqAccordion
