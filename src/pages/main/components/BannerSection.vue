<script setup lang="ts">
async function handleNavigation(selector: string) {
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
</script>

<template>
  <div
    id="banner-section"
    class="banner-section relative overflow-hidden pt-[var(--nav-bar-height)] md:h-949 h-1000"
  >
    <div class="area md:pt-90 pt-100 md:px-0 px-50">
      <div class="text-88 font-semibold w-678 lh-100 mb-40">Your Gatway To Go Global</div>
      <div
        class="md:text-20 text-35 lh-50 md:lh-30 text-[rgba(33,21,81,0.5)] w-690 mb-40"
      >
        We empower businesses to transact globally with seamless onboarding and end-to-end
        payment integration. Our gateway combines global expertise with a strong local
        presence to ensure secure, efficient, and reliable transactions.
      </div>
      <div
        class="hover-scale md:w-187 w-350 md:h-69 h-100 border-rd-8 bg-[#47D7AC] md:text-24 text-35 flex items-center justify-center font-semibold cursor-pointer"
        @click="handleNavigation('contact-section')"
      >
        Contact Us
      </div>
      <div
        class="w-235 h-96 border-rd-17 bg-[rgba(255,255,255,0.8)] items-center justify-center gap-18 px-20 absolute right-430 top-450 z-2 md:flex hidden"
      >
        <img
          src="@/assets/images/home/icon-banner-safe.svg"
          alt="banner-img"
          class="w-auto h-64"
        />
        <div class="text-20 lh-24 text-#595959">Secure Payments</div>
      </div>
      <div
        class="w-294 h-82 border-rd-17 bg-[rgba(255,255,255,0.8)] items-center justify-center gap-10 px-20 absolute -right-40 top-350 z-2 md:flex hidden"
      >
        <img
          src="@/assets/images/home/icon-banner-good.svg"
          alt="banner-img"
          class="w-auto h-44"
        />
        <div class="text-20 lh-24 text-#595959">24/7 Expert Support</div>
      </div>
      <div
        class="w-222 h-145 border-rd-17 bg-[rgba(255,255,255,0.8)] flex-col items-center justify-center gap-20 px-20 absolute right-320 top-650 z-2 md:flex hidden"
      >
        <img
          src="@/assets/images/home/icon-banner-time.svg"
          alt="banner-img"
          class="w-auto h-44"
        />
        <div class="text-20 lh-24 text-#595959">99.99% Uptime</div>
      </div>
      <img
        src="@/assets/images/home/post-banner.webp"
        alt="banner-img"
        class="w-auto absolute -md:right-110 -right-230 -md:top-50 top-50 md:h-960 h-1000"
      />
      <img
        src="@/assets/images/home/icon-banner-record.svg"
        alt="banner-img"
        class="w-auto absolute right-370 top-100 h-130 md:block hidden"
      />
    </div>
  </div>
</template>

<style lang="less" scoped>
.banner-section {
  background: url("@/assets/images/home/bg-banner.webp") no-repeat center top / 100% auto;
}
@media (max-width: 768px) {
  .banner-section {
    background-size: 200% auto;
  }
}
</style>
