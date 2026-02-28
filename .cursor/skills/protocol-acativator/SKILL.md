---
name: protocol-page
description: >
  生成Vue协议页面（动态加载HTML协议文档，协议文件已放在public/下）。当用户要求创建协议页、agreement页、terms页、隐私政策页、法律文档查看页，或提到"协议页面"、"协议页"、"protocol page"、"agreement page"、"加个协议页"等关键词时，使用此skill。
---

# 协议页面生成器

在 `pages/` 下创建一个 Vue 页面，用于 fetch 并渲染 HTML 协议文档。协议文件已放在 `public/` 下，开发环境直接访问本地文件，生产环境用远程 URL。不需要配置 Vite 代理。

## 参数

| 参数 | 说明 | 默认值 |
|---|---|---|
| 生产域名 | 生产环境托管HTML文件的远程域名 | `https://h5.lendmaxng.com` |
| 协议列表 | `{ label, tag, devFilename, prodUrl }` 数组 | 见下方 |
| 文件夹名 | 从 `docs`、`document`、`files`、`agreement` 中**随机选一个**，不询问用户 | 随机 |

**默认协议列表：**
```
{ label: "Terms of use",   tag: "terms",    devFilename: "privacy.html",  prodUrl: "https://h5.lendmaxng.com/termOfService.html" }
{ label: "Privacy Policy",  tag: "privacy",  devFilename: "terms.html", prodUrl: "https://h5.lendmaxng.com/privacy_policy.html" }
{ label: "Loan Contract",   tag: "contract", devFilename: "contract.html",  prodUrl: "https://h5.lendmaxng.com/loanAgreement.html" }
```

用户提供了就用用户的，没提供就用默认值。可以只提供部分参数。

## 执行步骤

### 1. 确认项目结构

检查项目用的是 `src/pages/` 还是 `pages/`，后续路径保持一致。

### 2. 生成页面文件

随机选一个文件夹名，创建 `<pages目录>/<文件夹名>/index.vue`，内容如下（替换变量部分）：

```vue
<script setup lang="ts">
const routes = useRoute()

const curIndex = ref(0)
const list = [
  // === 替换：根据协议列表生成 ===
  { label: 'Terms of use', tag: 'terms' },
  { label: 'Privacy Policy', tag: 'privacy' },
  { label: 'Loan Contract', tag: 'contract' },
]

const htmlContent = ref('')
const loading = ref(false)

const isDev = import.meta.env.DEV
const urlMap: Record<string, string> = {
  // === 替换：DEV用本地public/下的文件名，PROD用远程完整URL ===
  terms: isDev ? `/terms.html` : 'https://h5.lendmaxng.com/termOfService.html',
  privacy: isDev ? `/privacy.html` : 'https://h5.lendmaxng.com/privacy_policy.html',
  contract: isDev ? `/contract.html` : 'https://h5.lendmaxng.com/loanAgreement.html',
}

const currentLabel = computed(() => {
  return list[curIndex.value]?.label
})

async function fetchContent(tag: string) {
  const url = urlMap[tag]
  if (!url)
    return

  loading.value = true
  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const html = await response.text()
    htmlContent.value = html
  }
  catch (error) {
    console.error('Failed to fetch content:', error)
    htmlContent.value = `<p style="color: red;">Failed to load content. Please try again later.</p>`
  }
  finally {
    loading.value = false
  }
}

watchEffect(() => {
  const { tag } = routes.query
  const index = list.findIndex(it => it.tag === tag)
  curIndex.value = index >= 0 ? index : 0

  const targetTag = tag && typeof tag === 'string' ? tag : list[0].tag
  fetchContent(targetTag)
})
</script>

<template>
  <div class="part">
    <div class="container">
      <div class="title">
        {{ currentLabel }}
      </div>
      <div class="content-box" data-aos="fade-down" data-aos-delay="200">
        <div v-if="loading" class="loading">
          Loading...
        </div>
        <div v-else class="html-content" v-html="htmlContent" />
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped>
.part {
  padding: 160px 0 50px;
  .container {
    max-width: 1200px;
    margin: 0 auto;
    .title {
      font-size: 44px;
      font-weight: bold;
      margin-bottom: 20px;
      text-align: center;
    }
    .content-box {
      padding: 30px 40px;
      font-size: 20px;
      position: relative;
      overflow: auto;
      color: #000;
      background: white;
      min-height: 400px;

      .loading {
        text-align: center;
        padding: 40px;
        color: #000;
        font-size: 16px;
      }

      .html-content {
        color: #000;
        font-size: 16px;
        line-height: 24px;

        :deep(h1),
        :deep(h2),
        :deep(h3),
        :deep(h4),
        :deep(h5),
        :deep(h6) {
          font-weight: bold;
          margin-top: 20px;
          margin-bottom: 10px;
          color: #000;
        }

        :deep(p) {
          margin-bottom: 15px;
          line-height: 24px;
        }

        :deep(ul),
        :deep(ol) {
          margin-bottom: 15px;
          padding-left: 20px;
        }

        :deep(li) {
          margin-bottom: 8px;
          line-height: 24px;
        }

        :deep(strong) {
          font-weight: bold;
        }
      }
    }
  }
}
</style>
```

模板中标注了 `=== 替换 ===` 的部分需要根据实际参数替换，其余代码原样保留。

### 3. 检查底部导航栏

生成完成后，检查公共的底部组件（如 `Footer.vue`、`Layout.vue` 等）是否有跳转到协议相关的链接或动作，如果有，需要根据刚才生成的页面路径来修改跳转路由。

### 4. 告知用户

告诉用户：选了哪个文件夹名、页面路径、访问方式（如 `/<文件夹名>?tag=terms`）。
