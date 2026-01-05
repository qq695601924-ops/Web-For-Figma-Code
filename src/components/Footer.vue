<script setup lang="ts">
import { COPYRIGHT, EMAIL } from "@/config/index";
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";

const router = useRouter();
const isVisible = ref(false);

const theme = ref("dark");

onMounted(() => {
  // 延迟一小段时间后显示，以确保DOM已完全加载
  setTimeout(() => {
    isVisible.value = true;
  }, 100);
});
// 监听路由变化
watch(router.currentRoute, (newRoute) => {
  if (["about", "remove"].some((route) => newRoute?.path?.indexOf(route) !== -1)) {
    theme.value = "dark";
  } else {
    theme.value = "light";
  }
});

async function handleNavigation(item: { selector: string }) {
  const { selector } = item;

  // 如果目标路由与当前路由不同，先进行路由跳转
  if (selector) {
    await nextTick();
    // 给页面渲染一些时间
    setTimeout(() => scrollToElement(selector), 100);
  }

  // 如果在同一页面且有选择器，直接滚动
  if (selector) scrollToElement(selector);
}

function scrollToElement(selector: string) {
  const element = document.querySelector(`#${selector}`);
  if (!element) {
    console.warn(`Element with id "${selector}" not found`);
    return;
  }

  element.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });
}

function gotoBlankPage(url: string) {
  window.open(url, "_blank");
}
</script>

<template>
  <transition name="fade-slide" appear>
    <div
      class="footer-wrapper relative overflow-hidden text-white bg-#211551 text-lighter"
    >
      <div class="area md:pt-50 pt-100 md:px-0 px-50">
        <div class="md:flex block justify-between">
          <div class="md:mb-0 mb-70">
            <img
              src="@/assets/images/common/logo-white.svg"
              alt="logo"
              class="w-auto md:h-32 h-80 mb-20 block"
            />
            <div
              class="md:w-300 w-full md:text-16 text-40 md:lh-24 lh-50 text-[rgba(255,255,255,0.65)]"
            >
              We empower businesses to transact globally with seamless onboarding and
              end-to-end payment integration. Our gateway combines global expertise with a
              strong local presence to ensure secure, efficient, and reliable
              transactions.
            </div>
          </div>
          <div>
            <div class="md:text-16 text-50 font-semibold md:mb-22 mb-40 text-white">
              Platform
            </div>
            <ul
              class="md:text-16 text-45 md:block flex gap-40 text-[rgba(255,255,255,0.65)]"
            >
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                v-if="false"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                API Documentation
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="gotoBlankPage('/PrivacyPolicy.html')"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Privacy Policy
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="gotoBlankPage('/TermsOfService.html')"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Terms of Service
              </li>
            </ul>
          </div>
          <div class="mt-0 mt-40">
            <div class="md:text-16 text-50 font-semibold md:mb-22 mb-40 text-white">
              Company
            </div>
            <ul
              class="md:text-16 text-45 md:block flex flex-wrap gap-20 text-[rgba(255,255,255,0.65)]"
            >
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="handleNavigation({ selector: 'banner-section' })"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Home
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="handleNavigation({ selector: 'why-section' })"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Advantages
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="handleNavigation({ selector: 'services-section' })"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Services
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="handleNavigation({ selector: 'map-section' })"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                Global Reach
              </li>
              <li
                class="flex items-center gap-4 mb-20 cursor-pointer hover:underline"
                @click="handleNavigation({ selector: 'about-section' })"
              >
                <img
                  src="@/assets/images/common/icon-arrow-right.svg"
                  alt="arrow-right"
                  class="w-auto md:h-16 h-60"
                />
                About
              </li>
            </ul>
          </div>
          <div class="md:mt-0 mt-40">
            <div class="md:text-16 text-50 font-semibold md:mb-22 mb-40 text-white">
              Contact
            </div>
            <ul
              class="md:text-16 text-45 md:block flex flex-wrap gap-20 text-[rgba(255,255,255,0.65)]"
            >
              <li class="flex items-center gap-4 mb-20">{{ EMAIL }}</li>
            </ul>
          </div>
        </div>
        <img
          src="@/assets/images/common/footer-logo.svg"
          alt="footer-bg"
          class="w-full h-auto block py-50"
        />
        <div
          class="md:text-16 text-40 text-center md:lh-60 lh-120 flex items-center justify-center"
          style="border-top: 1px solid rgba(255, 255, 255, 0.1)"
        >
          {{ COPYRIGHT }}
        </div>
      </div>
    </div>
  </transition>
</template>

<style lang="less" scoped>
/* 渐入动画 */
.fade-slide-enter-active,
.fade-slide-appear-active {
  transition: all 300ms ease;
}

.fade-slide-enter-from,
.fade-slide-appear-from {
  opacity: 0;
  transform: translateY(30px);
}
</style>
