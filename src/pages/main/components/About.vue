<script setup lang="ts">
import { APP_NAME } from "@/config/index";
import postAbout1 from "@/assets/images/home/post-about-1.webp";
import postAbout2 from "@/assets/images/home/post-about-2.webp";
import postAbout3 from "@/assets/images/home/post-about-3.webp";
import ArrowRightActive from "@/assets/images/home/icon-arrow-right-active.webp";
import ArrowRight from "@/assets/images/home/icon-arrow-right.webp";

const step = [
  {
    title: "About",
    image: postAbout1,
    desc:
      "We are an international payment service provider (PSP) working with local partners worldwide to deliver localized payment solutions to global clients. We specialize in international merchants and focus on Alternative Payment Methods (APMs), including online banking, ATM cards, e-wallets, QR payments, and OTC transactions, with global card acquiring as a key strategic focus.",
  },
  {
    title: "Purpuse",
    image: postAbout2,
    desc:
      "To simplify global payments and remove barriers in complex and emerging markets, enabling businesses to accept payments securely and efficiently anywhere in the world.",
  },
  {
    title: "Ambition",
    image: postAbout3,
    desc:
      "To build a globally connected payment infrastructure that bridges international card networks and trusted local payment systems, powering long-term growth for businesses worldwide.",
  },
];

const currentIndex = ref(0);

function changeIndex(index: number) {
  // 优雅写法，考虑边界
  currentIndex.value = Math.max(0, Math.min(index, step.length - 1));
}
</script>

<template>
  <div
    id="about-section"
    class="about-section py-100 md:h-818 h-1600"
    style="scroll-margin-top: 100px"
  >
    <div class="area">
      <div class="md:text-48 text-88 font-bold text-center md:mb-40 mb-70">
        About {{ APP_NAME }}
      </div>
      <div
        class="flex gap-40 absolute step-wrapper transition-all duration-200"
        :data-index="currentIndex"
      >
        <div
          v-for="(item, index) in step"
          :key="item.title"
          class="md:w-540 w-800 md:h-558 h-900 rounded-12 relative"
        >
          <div class="w-full md:h-266 md:h-300 h-400 relative">
            <img :src="item.image" alt="about-1" class="w-full h-full object-cover" />
            <div
              class="w-full md:h-59 h-100 absolute bg-#0000006e left-0 bottom-0 backdrop-blur-3 md:text-24 text-40 text-white flex items-center px-35 transition-all duration-400 opacity-100"
              :class="{
                '!opacity-0 ': currentIndex === index,
                'rounded-[0px_0px_12px_12px]': currentIndex !== index,
              }"
            >
              {{ item.title }}
            </div>
          </div>
          <div
            class="md:flex hidden w-88 h-88 bg-#FFFFFF rounded-full absolute left-25 top-240 items-center justify-center transition-all duration-200 opacity-0 z-2"
            style="box-shadow: 0px 50px 60px -10px rgba(0, 0, 0, 0.08)"
            :class="{ '!opacity-100': currentIndex === index }"
          >
            <img
              src="@/assets/images/home/icon-quote.svg"
              alt="quote"
              class="w-35% h-auto"
            />
          </div>
          <div
            class="w-full md:h-292 h-800 relative bg-white px-35 py-45 transition-all duration-400 opacity-0 rounded-[0px_0px_12px_12px]"
            :class="{ 'opacity-100': currentIndex === index }"
          >
            <div class="md:text-24 text-55 text-semibold text-#1B152B md:mb-15 mb-30">
              {{ item.title }}
            </div>
            <div class="md:text-16 text-40 text-[rgba(27,21,43,0.5)] md:lh-24 lh-55">
              {{ item.desc }}
            </div>
          </div>
        </div>
      </div>

      <img
        :src="currentIndex === 0 ? ArrowRight : ArrowRightActive"
        alt="arrow"
        class="w-auto md:h-64 h-120 absolute right-350 md:top-500 top-700 rotate-180 cursor-pointer"
        @click="changeIndex(currentIndex - 1)"
      />
      <img
        :src="currentIndex === step.length - 1 ? ArrowRight : ArrowRightActive"
        alt="arrow"
        class="w-auto md:h-64 h-120 absolute md:right-250 right-150 md:top-500 top-700 cursor-pointer"
        @click="changeIndex(currentIndex + 1)"
      />
    </div>
  </div>
</template>

<style lang="less" scoped>
.about-section {
  background: url("@/assets/images/home/bg-about.webp") no-repeat center bottom / 100%
    auto;
}
.step-wrapper {
  &[data-index="0"] {
    transform: translateX(0);
  }
  &[data-index="1"] {
    transform: translateX(-580px);
  }
  &[data-index="2"] {
    transform: translateX(-1160px);
  }
}

@media (max-width: 768px) {
  .step-wrapper {
    &[data-index="0"] {
      transform: translateX(50px);
    }
    &[data-index="1"] {
      transform: translateX(-750px);
    }
    &[data-index="2"] {
      transform: translateX(-1600px);
    }
  }
}
</style>
