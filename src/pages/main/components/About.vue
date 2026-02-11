<script setup lang="ts">
import { APP_NAME } from "@/config/index";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
import postAbout1 from "@/assets/images/home/post-about-1.webp";
import postAbout2 from "@/assets/images/home/post-about-2.webp";
import postAbout3 from "@/assets/images/home/post-about-3.webp";
import ArrowRightActive from "@/assets/images/home/icon-arrow-right-active.webp";

const step = [
  {
    title: "About Optivolve Digital",
    image: postAbout1,
    desc: "Optivolve Digital is a technology-driven company focused on enabling seamless, secure, and scalable transaction solutions for businesses worldwide. We build robust infrastructure that simplifies how value moves across markets, helping organizations operate efficiently in an increasingly connected global economy.\nBy combining innovation, reliability, and compliance-first principles, Optivolve Digital empowers businesses to grow with confidence.",
  },
  {
    title: "Our Ambition",
    image: postAbout2,
    desc: "Our ambition is to become a trusted local transaction partner for businesses across Pakistan. Optivolve Digital is committed to simplifying payment processes, reducing operational complexity, and delivering reliable solutions that support sustainable business growth in the local market.\nAs transaction needs evolve, we continuously enhance our platform to align with Pakistan's regulatory environment, user behaviors, and emerging business models—ensuring our services remain secure, efficient, and future-ready.",
  },
  {
    title: "Our Purpose",
    image: postAbout3,
    desc: "Our purpose is to make transactions simpler, safer, and more accessible. Optivolve Digital exists to help businesses move value with clarity and control, while maintaining the highest standards of security and compliance.\n    By building technology that prioritizes trust and transparency, we strive to support sustainable growth for our partners and contribute to a more connected financial ecosystem.",
  },
];

const currentIndex = ref(0);
const swiperRef = ref();

const modules = [Navigation];

function onSwiper(swiper: any) {
  swiperRef.value = swiper;
}

function onSlideChange(swiper: any) {
  currentIndex.value = swiper.realIndex;
}

function changeIndex(direction: number) {
  if (swiperRef.value) {
    if (direction > 0) {
      swiperRef.value.slideNext();
    } else {
      swiperRef.value.slidePrev();
    }
  }
}
</script>

<template>
  <div
    id="about-section"
    class="about-section py-100 md:h-900 h-1900 md:px-0 px-100"
    style="scroll-margin-top: 100px"
  >
    <div class="md:text-48 text-88 font-bold text-center md:mb-40 mb-70">
      About {{ APP_NAME }}
    </div>
    <div class="relative md:mx-30 mx-0">
      <Swiper
        :modules="modules"
        :slides-per-view="1"
        :space-between="60"
        :centered-slides="true"
        :loop="true"
        :allow-touch-move="true"
        :breakpoints="{
          768: {
            slidesPerView: 3,
          },
        }"
        class="about-swiper h-auto"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
      >
        <SwiperSlide
          v-for="(item, index) in [...step, ...step]"
          :key="`${item.title}-${index}`"
          class="md:w-540 w-800 relative rounded-12 transition-all duration-200 pt-30"
        >
          <div
            class="w-full md:h-240 h-500 relative rounded-[12px_12px_0_0] overflow-hidden"
          >
            <img :src="item.image" alt="about-1" class="w-full h-full object-cover" />
          </div>
          <div
            class="md:flex hidden w-88 h-88 bg-#FFFFFF rounded-full absolute left-15 top-210 items-center justify-center transition-all duration-200 z-2"
            style="box-shadow: 0px 50px 60px -10px rgba(0, 0, 0, 0.08)"
          >
            <img
              src="@/assets/images/home/icon-quote.svg"
              alt="quote"
              class="w-35% h-auto"
            />
          </div>
          <div
            class="md:h-340 h-700 w-full relative bg-white px-20 py-45 transition-all duration-400 rounded-[0px_0px_12px_12px]"
          >
            <div class="md:text-24 text-55 text-semibold text-#1B152B md:mb-10 mb-30">
              {{ item.title }}
            </div>
            <div
              class="md:text-15 text-40 text-[rgba(27,21,43,0.5)] md:lh-20 lh-55 whitespace-pre-wrap"
            >
              {{ item.desc }}
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
      <div class="flex items-center justify-center gap-50 md:mt-30 mt-50" v-if="false">
        <img
          :src="ArrowRightActive"
          alt="arrow"
          class="w-auto md:h-64 h-120 rotate-180 cursor-pointer z-10"
          @click="changeIndex(-1)"
        />
        <img
          :src="ArrowRightActive"
          alt="arrow"
          class="w-auto md:h-64 h-120 cursor-pointer z-10"
          @click="changeIndex(1)"
        />
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped>
.about-section {
  background: url("@/assets/images/home/bg-about.webp") no-repeat center bottom / cover;
}

:deep(.about-swiper) {
  .swiper-slide {
    width: auto;
    height: auto;
  }
}

@media (max-width: 768px) {
  .about-section {
    .swiper-slide.swiper-slide-active {
      transform: scale(1);
    }
  }
}
</style>
