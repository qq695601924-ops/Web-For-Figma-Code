---
name: vue-layout-converter
description: 将 Vue SFC 模板中基于 absolute 定位的布局转换为 flex 自动布局。当用户提供含 absolute/top-X/left-X 等 Tailwind 定位类的 Vue 文件，要求转为弹性布局时触发。关键词包括：去掉绝对定位、转flex布局、自动撑开、修复布局、AI生成的代码布局优化。
---

# Vue 绝对定位转 Flex 布局转换器

你要将 Vue SFC 模板从坐标式绝对定位转换为语义化的 flex 布局。输入是一个 Vue 文件，其中元素使用了 `absolute`、`top-[X]`、`left-[X]`、`w-[X]`、`h-[X]`、`min-h-[X]` 等 Tailwind 类，父容器为 `relative`。

## 核心算法

按以下步骤**依次执行**，不要跳步。

### 第一步：提取空间数据

对每个带 `absolute` 的元素，提取边界框：

```
{ top, left, width, height, right: left+width, bottom: top+height }
```

从 Tailwind 类中解析数值，常见格式：

- `top-489` → top: 489
- `left-[188px]` → left: 188
- `w-851` → width: 851
- `h-668` → height: 668

同时提取父容器的尺寸（`min-h-[X]`、`w-[X]`/`h-[X]`）。

### 第二步：判断父子包含关系

检查是否有元素完全包含另一个元素：

```
A 包含 B 的条件：
  B.left >= A.left 且 B.top >= A.top 且
  B.right <= A.right 且 B.bottom <= A.bottom
```

存在包含关系时，B 成为 A 的子元素。否则所有绝对定位元素都是根容器的兄弟。

### 第三步：兄弟元素按行或列分组

对同一父级下的兄弟元素，判断排列方向：

**水平行** — `top` 值相近（差值 < 50px）：
→ 父容器用 `flex flex-row`，子元素按 `left` 排序。

**垂直列** — `left` 值相近（差值 < 50px）：
→ 父容器用 `flex flex-col`，子元素按 `top` 排序。

**混合排列** — `top` 和 `left` 都不对齐，且不重叠：
→ 两步处理：

  1. 按 `top` 排序，将 top 差值 < 50px 的归为一"行"
  2. 每行内按 `left` 排序
  3. 外层 `flex flex-col` 包裹各行，每行内部 `flex flex-row`

### 第四步：处理重叠元素

两个元素的边界框相交、但互不完全包含时，视为重叠。

处理方式：面积更大或 DOM 顺序靠前的元素正常参与 flex 布局。重叠的元素作为**装饰层** — 保留 `absolute`，但将其包裹在一个参与 flex 流的 `relative` 容器中。

```html
<!-- 重叠场景：图片与内容区重叠 -->
<div class="relative flex-shrink-0">
  <img class="w-588 h-668" ... />
</div>
```

### 第五步：计算间距

将像素偏移转换为 `gap`、`padding`、`margin`：

| 关系 | 来源 | 转换为 |
|---|---|---|
| 首个子元素到父边缘的偏移 | `child.left - parent.left`、`child.top - parent.top` | 父容器的 `padding` |
| 兄弟之间的间距 | 行：`next.left - prev.right`；列：`next.top - prev.bottom` | 父容器的 `gap` |
| 多个 gap 差值 < 8px | 取平均值 | 统一 `gap` |
| gap 差值较大 | 保留各自值 | 每个子元素的 `margin` |

**水平居中检测：**

计算内容区域的左右留白：

- `leftSpace = child.left - parent.left`
- `rightSpace = parent.width - child.right`

| 条件 | 策略 |
|---|---|
| `abs(leftSpace - rightSpace) < 30px` | 用 `mx-auto` + `max-w-[内容宽]`，实现居中自适应 |
| `abs(leftSpace - rightSpace) >= 30px` | 保持 `pl-*`，忠实还原原始偏移 |

### 第六步：确定尺寸策略

| 条件 | 策略 |
|---|---|
| 图片且有明确宽高 | 保留固定尺寸，加 `shrink-0` |
| 子元素宽度 ≈ 父元素宽度（>90%） | 用 `w-full` |
| 两个兄弟大致平分父宽度 | 弹性一方用 `flex-1` |
| 纯文本内容 | 去掉固定宽高，让内容撑开 |
| 文本容器的固定高度 | 去掉 `h-[X]`，除非是视觉上必要的最小高度 |

### 第七步：清理类名

**删除：**

- `absolute`、根容器不再需要的 `relative`
- `top-*`、`left-*`、`right-*`、`bottom-*`
- 根容器的 `min-h-[X]`（由内容撑开高度）
- `rounded-0`（无视觉效果，属于噪声）
- 文本容器的固定 `w-[X]` / `h-[X]`（除非是有意的 max-width）

**保留：**

- 颜色、字体、字号、背景等视觉类
- 内部元素原有的 `flex`、`gap`、`justify-*`、`items-*`
- 组件 props 和指令（`v-for`、`:key` 等）

### 第八步：组装并验证

转换完成后，逐项检查：

1. 除了装饰层（包裹在 `relative` 内），没有元素使用 `absolute`
2. 根容器没有 `min-h-[X]` — 高度由内容决定
3. 视觉阅读顺序与 DOM 顺序一致（上→下、左→右）
4. 所有原始组件和内容完整保留 — 只改了布局类

## 输出规则

- 输出完整的 Vue SFC（`<script setup>` + `<template>`），不省略任何部分
- 不修改 `<script setup>` — 只转换 `<template>` 部分
- 在每个主要区块上方加简短注释，说明布局决策
- 保持 Tailwind 类的写法风格与原文一致

## 示例

**转换前：**

```html
<div class="min-h-800 bg-white relative">
  <h1 class="absolute left-100 top-60 text-48 font-bold">标题</h1>
  <p class="absolute left-100 top-130 text-16">副标题</p>
  <img class="w-300 h-300 absolute left-50 top-250" src="..." />
  <div class="w-500 absolute left-400 top-250">卡片内容</div>
</div>
```

**分析过程：**

- h1(left:100, top:60) 和 p(left:100, top:130) → left 相同，垂直排列 → 标题组
- img(left:50, top:250) 和 div(left:400, top:250) → top 相同，水平排列 → 内容行
- 标题组 top:60–146，内容行 top:250 → 两个垂直区块

**转换后：**

```html
<!-- 根容器：垂直堆叠，保留背景，去掉 min-h -->
<div class="bg-white flex flex-col px-50 pt-60 gap-104">
  <!-- 标题组：垂直排列 -->
  <div class="flex flex-col gap-22 pl-50">
    <h1 class="text-48 font-bold">标题</h1>
    <p class="text-16">副标题</p>
  </div>
  <!-- 内容行：左图右卡片 -->
  <div class="flex flex-row gap-50 items-start">
    <img class="w-300 h-300 shrink-0" src="..." />
    <div class="flex-1">卡片内容</div>
  </div>
</div>
```
