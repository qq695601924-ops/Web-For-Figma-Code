---
name: vue-static-to-interactive-footer
description: 将AI生成的静态Vue组件代码改造为可交互的生产级代码。当用户提到"静态改交互"、"AI生成的代码需要改造"、"footer/header/nav加交互"、"提取公共变量"、"加路由跳转"等场景时触发。
---

# 静态Vue组件 → 交互式组件改造

将AI Coding工具生成的纯静态Vue组件改造为可交互组件。核心任务：把"看起来像"变成"用起来像"。

## 改造步骤

### 1. 提取公共变量

将硬编码的品牌名、邮箱、工作时间、版权声明等文案提取到 `@/config/index`，模板中用 `{{ VAR }}` 替换。

```vue
<!-- 改造前 -->
<span>SeguroCash</span>
<span>soporte@segurocash.com</span>

<!-- 改造后 -->
<script setup lang="ts">
import { APP_NAME, EMAIL } from "@/config/index";
</script>
<span>{{ APP_NAME }}</span>
<span>{{ EMAIL }}</span>
```

仅提取跨组件复用的文案，只出现一次的描述段落保留原样。

### 2. 添加路由跳转

导航链接和底部法律链接从纯文本改为可点击跳转。

```vue
<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();
function goto(path: any) {
  router.push(path);
}
</script>

<!-- 改造前 -->
<span>Ayuda</span>

<!-- 改造后 -->
<div class="cursor-pointer hover:underline" @click="goto({ path: 'help' })">Ayuda</div>
```

路由路径不确定时，主动向用户确认。

### 3. 补充交互事件

为看起来像按钮但无事件的元素绑定行为：
- 复制按钮 → 剪贴板复制 + 反馈提示
- 应用商店图标 → 外链跳转
- 底部法律链接 → 路由跳转（带query参数）

### 4. 清理AI代码通病

- 去掉不必要的固定宽高（`w-145 h-22`），让内容自然撑开
- 绝对定位改为flex布局
- 无意义hash图片名替换为语义化资源（如有SVG可用）
