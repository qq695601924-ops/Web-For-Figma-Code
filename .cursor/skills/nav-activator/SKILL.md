---
name: navbar-functional
description: 将静态导航栏代码改造为具备路由跳转和当前页面激活高亮功能的动态导航栏。当用户要求生成头部导航栏(navbar/header/nav)组件时，或要求为已有静态导航栏添加跳转、选中、激活状态功能时，必须使用此skill。适用于 Vue3 + Vue Router + UnoCSS/Tailwind 技术栈。
---

# Navbar Functional 导航栏功能化

## 目标

将纯静态的导航栏模板代码，改造为具备 **路由跳转** 和 **当前激活页面高亮** 的功能性导航栏。

## 规则

### 1. 菜单数据必须来自配置文件

禁止在组件中硬编码菜单项。菜单列表必须从统一配置导入：

```ts
import { menuList } from "@/config/index";
import type { MenuItem } from "@/config/index";
```

`MenuItem` 类型定义：

```ts
interface MenuItem {
  name: string;    // 显示文本
  path: string;    // 路由路径
  selector?: string; // 可选，页内锚点id
}
```

如果项目中尚无此配置文件，需同时创建 `@/config/index.ts` 并导出 `menuList`，根据导航栏中的菜单项内容填充。

### 2. 使用 Vue Router 实现路由跳转

```ts
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
```

### 3. 激活状态判断逻辑

```ts
function isActive(path: string): boolean {
  if (path === "/" && route.path === "/") return true;
  return path !== "/" && route.path.startsWith(path);
}
```

在模板中通过动态 class 绑定激活样式。使用页面中**已有的高亮颜色**作为激活色，例如原代码中某个菜单项是 `text-[#de2e2d]`，则激活样式为：

```html
:class="{ 'text-[#de2e2d]': isActive(item.path) }"
```

### 4. 导航跳转处理（支持锚点）

```ts
async function handleNavigation(item: MenuItem) {
  const { path, selector } = item;

  if (path && path !== route.path) {
    await router.push(path);
    if (selector) {
      await nextTick();
      setTimeout(() => scrollToElement(selector), 100);
    }
    return;
  }

  if (selector) scrollToElement(selector);
}

function scrollToElement(selector: string) {
  const element = document.querySelector(`#${selector}`);
  if (!element) return;
  element.scrollIntoView({ behavior: "smooth", block: "start" });
}
```

### 5. 模板改造要点

将硬编码的多个 `<span>` 菜单项替换为 `v-for` 循环：

```html
<div
  v-for="item in menuList"
  :key="item.name"
  class="flex items-center"
>
  <span
    class="cursor-pointer transition-colors duration-300"
    :class="{ 'text-[激活色]': isActive(item.path) }"
    @click="handleNavigation(item)"
  >
    {{ item.name }}
  </span>
</div>
```

### 6. 禁止为菜单项设置固定宽度

原始静态代码中每个菜单项可能带有 `w-53`、`w-97`、`w-148` 等固定宽度 class，这是因为静态代码按视觉稿像素硬编码的结果。改造时**必须移除所有菜单项的固定宽度**，原因：

- 菜单文本内容可能变化，固定宽度会导致截断或留白
- `MenuItem` 类型中**不允许添加** `width`、`className`、`style` 等样式属性，配置文件只保留 `name`、`path`、`selector`

替代方案：让文本自适应宽度，如需间距用父容器的 `gap` 控制。

### 7. 保持原有样式不变

改造过程中必须保留原代码的所有视觉样式（颜色、字号、间距、布局、圆角、阴影等），只替换逻辑部分。

## 检查清单

- [ ] `<script setup>` 中导入了 `useRoute`、`useRouter`、`menuList`
- [ ] 实现了 `isActive` 函数
- [ ] 实现了 `handleNavigation` 函数
- [ ] 模板中使用 `v-for` 渲染菜单项，而非硬编码
- [ ] 激活项有动态 class 绑定
- [ ] 菜单项绑定了 `@click="handleNavigation(item)"`
- [ ] 菜单项无固定宽度 class（如 `w-53`），MenuItem 类型无样式属性
- [ ] 原有样式完整保留
- [ ] 如项目缺少 `@/config/index.ts`，已同时创建
