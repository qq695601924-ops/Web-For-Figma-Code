<script setup lang="ts">
interface FaqItem {
  title: string
  content: string
}

const props = withDefaults(defineProps<{
  list: FaqItem[]
  defaultOpen?: number
  accordion?: boolean
}>(), {
  defaultOpen: undefined,
  accordion: false,
})

// 手风琴模式：单个 index | null
// 独立模式：Set 存储多个 index
const activeIndex = ref<number | null>(props.defaultOpen ?? null)
const activeSet = ref<Set<number>>(new Set(props.defaultOpen !== undefined ? [props.defaultOpen] : []))

const collapseRefs = ref<HTMLDivElement[]>([])
let TITLE_HEIGHT = 76

function isOpen(index: number): boolean {
  return props.accordion
    ? activeIndex.value === index
    : activeSet.value.has(index)
}

function expand(el: HTMLDivElement) {
  el.style.height = 'auto'
  const { height } = el.getBoundingClientRect()
  el.style.height = `${TITLE_HEIGHT}px`
  el.getBoundingClientRect()
  el.style.transition = 'height background-color color 0.3s ease-in-out'
  el.style.height = `${height}px`
}

function collapse(el: HTMLDivElement) {
  el.style.height = `${el.scrollHeight}px`
  el.getBoundingClientRect()
  el.style.transition = 'height background-color color 0.3s ease-in-out'
  el.style.height = `${TITLE_HEIGHT}px`
}

function toggle(index: number) {
  if (props.accordion) {
    toggleAccordion(index)
  }
  else {
    toggleIndependent(index)
  }
}

function toggleAccordion(index: number) {
  const prev = activeIndex.value
  activeIndex.value = activeIndex.value === index ? null : index

  nextTick(() => {
    // 收起之前展开的
    if (prev !== null && prev !== index && collapseRefs.value[prev]) {
      collapse(collapseRefs.value[prev])
    }

    // 展开当前点击的
    if (activeIndex.value !== null) {
      expand(collapseRefs.value[activeIndex.value])
    }

    // 点击已展开项 -> 收起自己
    if (activeIndex.value === null && prev !== null && collapseRefs.value[prev]) {
      collapse(collapseRefs.value[prev])
    }
  })
}

function toggleIndependent(index: number) {
  const wasOpen = activeSet.value.has(index)

  if (wasOpen) {
    activeSet.value.delete(index)
  }
  else {
    activeSet.value.add(index)
  }
  // 触发响应式更新
  activeSet.value = new Set(activeSet.value)

  nextTick(() => {
    const el = collapseRefs.value[index]
    if (!el)
      return
    wasOpen ? collapse(el) : expand(el)
  })
}

function onTransitionEnd(index: number) {
  const el = collapseRefs.value[index]
  if (!el)
    return
  if (isOpen(index)) {
    el.style.height = 'auto'
  }
}

onMounted(() => {
  if (props.defaultOpen !== undefined && props.defaultOpen !== null) {
    nextTick(() => {
      const el = collapseRefs.value[props.defaultOpen!]
      if (el) {
        el.style.height = 'auto'
      }
    })
  }
  TITLE_HEIGHT = collapseRefs.value[0].getBoundingClientRect().height
})
</script>

<template>
  <div
    v-for="(item, index) in list"
    :key="index"
    :ref="(el) => { if (el) collapseRefs[index] = el as HTMLDivElement }"
    class="collapse mb-20 h-76 cursor-pointer overflow-hidden rounded-16 px-40 transition-all duration-250 md:mb-20 md:h-76"
    :class="isOpen(index) ? 'bg-[#de2e2d]' : 'bg-[#ffffff]'"
    @click="toggle(index)"
    @transitionend="onTransitionEnd(index)"
  >
    <!-- 标题栏 -->
    <div class="relative flex items-center justify-between lh-76 md:lh-76">
      <div
        class="h-76 w-92% flex items-center text-20 lh-30 transition-all duration-250"
        :class="isOpen(index) ? 'text-[#ffffff]' : 'text-[#16171c]'"
      >
        <b>{{ item.title }}</b>
      </div>
      <div
        class="absolute top-50% h-76 w-64 flex items-center justify-center transition-all duration-250 -right-15 md:h-76 -translate-y-1/2"
      >
        <img
          v-if="isOpen(index)"
          src="@/assets/images/ayuda/ayuda-q5r6s7t8.png"
          alt="arrow"
          class="h-6 w-13"
        >
        <img
          v-else
          src="@/assets/images/ayuda/ayuda-u9v0w1x2.png"
          alt="arrow"
          class="h-6 w-13"
        >
      </div>
    </div>

    <!-- 内容区 -->
    <div
      class="mb-40 mr-70 whitespace-pre-wrap text-16 text-[rgba(255,255,255,0.65)] font-400 lh-24 md:mr-50"
    >
      {{ item.content }}
    </div>
  </div>
</template>
