---
name: vue-download-unify
description: 为页面中静态的应用商店下载元素添加点击和hover交互。当页面中出现Google Play、App Store相关的图片、按钮、badge等静态元素时触发。不限于footer，页面任何位置的下载元素都适用。
---

# 下载按钮交互绑定

为页面中静态的下载元素统一添加点击跳转和鼠标hover交互，不修改原有样式。

## 改造步骤

### 1. 提取下载地址到配置

将硬编码的Google Play链接提取到 `@/config/index`，组件中引入使用。

```ts
// @/config/index
export const GOOGLE_PLAY_URL = "https://play.google.com/store/apps/details?id=xxx";
```

### 2. 为下载元素添加交互

保持原有样式不变，添加点击行为和hover反馈。

```vue
<script setup lang="ts">
import { GOOGLE_PLAY_URL } from "@/config/index";

function openDownload() {
  window.open(GOOGLE_PLAY_URL, "_blank", "noopener,noreferrer");
}
</script>

<!-- 改造前 -->
<img src="@/assets/images/layout/footer-d4f6k8l0.png" class="w-112 h-32" alt="googleplay" />

<!-- 改造后 -->
<div role="link" aria-label="Descargar en Google Play" @click="openDownload" class="cursor-pointer hover:opacity-80">
  <img src="@/assets/images/layout/footer-d4f6k8l0.png" class="w-112 h-32" alt="Google Play" />
</div>
```

### 3. hover交互

在不改变原有样式的前提下，追加以下效果，必须带 `transition` 过渡使动画平滑：

```vue
<!-- 基础：cursor + 过渡 -->
class="... cursor-pointer transition-all duration-300"

<!-- 可选：加1.15倍放大（非必须，随机使用以丰富交互层次） -->
class="... cursor-pointer transition-all duration-300 hover:scale-[1.15]"
```

不要添加颜色变化、下划线等会影响原有视觉的样式。

### 4. 语义化补充

用 `role="link"` + `aria-label` 包裹下载元素，让交互意图明确：

```vue
<div role="link" aria-label="Descargar en Google Play" @click="openDownload">
  ...
</div>
```

## 适用范围

不仅是footer，页面**任何位置**出现应用商店下载元素都需要改造。识别特征：

- 文案包含 `Google Play` / `GooglePlay` / `App Store` / `Descargar`
- 图片alt包含 `google` / `play` / `app store` 等关键词
- 明显的商店badge图片

**示例：页面中部的下载按钮同样适用**

```vue
<!-- 改造前：静态展示 -->
<div class="flex items-center gap-16 rounded-88 bg-[#de2e2d] px-32 py-16">
  <img src="@/assets/images/inicio/inicio-h0l2j9e7.png" class="h-48 w-48" alt="Google Play">
  <span class="text-32 text-[#f2f2f4]">GooglePlay</span>
</div>

<!-- 改造后 -->
<div role="link" aria-label="Descargar en Google Play"
     @click="openDownload"
     class="flex items-center gap-16 rounded-88 bg-[#de2e2d] px-32 py-16 cursor-pointer transition-all duration-300 hover:scale-[1.15]">
  <img src="@/assets/images/inicio/inicio-h0l2j9e7.png" class="h-48 w-48" alt="Google Play">
  <span class="text-32 text-[#f2f2f4]">GooglePlay</span>
</div>
```
