<script setup lang="ts">
import { APP_NAME } from '@/config/index'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Navigation } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/navigation'
import postAbout1 from '@/assets/images/home/post-about-1.webp'
import postAbout2 from '@/assets/images/home/post-about-2.webp'
import postAbout3 from '@/assets/images/home/post-about-3.webp'
import ArrowRightActive from '@/assets/images/home/icon-arrow-right-active.webp'

const step = [
  {
    title: 'About Optivolve Digital',
    image: postAbout1,
    desc: 'Optivolve Digital is a technology-driven company focused on enabling seamless, secure, and scalable transaction solutions for businesses worldwide. We build robust infrastructure that simplifies how value moves across markets, helping organizations operate efficiently in an increasingly connected global economy.\nBy combining innovation, reliability, and compliance-first principles, Optivolve Digital empowers businesses to grow with confidence.',
  },
  {
    title: 'Our Ambition',
    image: postAbout2,
    desc: 'Our ambition is to become a trusted local transaction partner for businesses across Pakistan. Optivolve Digital is committed to simplifying payment processes, reducing operational complexity, and delivering reliable solutions that support sustainable business growth in the local market.\nAs transaction needs evolve, we continuously enhance our platform to align with Pakistan\'s regulatory environment, user behaviors, and emerging business models—ensuring our services remain secure, efficient, and future-ready.',
  },
  {
    title: 'Our Purpose',
    image: postAbout3,
    desc: 'Our purpose is to make transactions simpler, safer, and more accessible. Optivolve Digital exists to help businesses move value with clarity and control, while maintaining the highest standards of security and compliance.\n    By building technology that prioritizes trust and transparency, we strive to support sustainable growth for our partners and contribute to a more connected financial ecosystem.',
  },
]

const currentIndex = ref(0)
const swiperRef = ref()

const modules = [Navigation]

function onSwiper(swiper: any) {
  swiperRef.value = swiper
}

function onSlideChange(swiper: any) {
  currentIndex.value = swiper.realIndex
}

function changeIndex(direction: number) {
  if (swiperRef.value) {
    if (direction > 0) {
      swiperRef.value.slideNext()
    }
    else {
      swiperRef.value.slidePrev()
    }
  }
}
</script>

<template>
  <div
    id="about-section"
    class="about-section h-1900 px-100 py-100 md:h-900 md:px-0"
    style="scroll-margin-top: 100px"
  >
    <div class="mb-70 text-center text-88 font-bold md:mb-40 md:text-48">
      About {{ APP_NAME }}
    </div>
    <div class="relative mx-0 md:mx-30">
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
        @slide-change="onSlideChange"
      >
        <SwiperSlide
          v-for="(item, index) in [...step, ...step]"
          :key="`${item.title}-${index}`"
          class="relative w-800 rounded-12 pt-30 transition-all duration-200 md:w-540"
        >
          <div
            class="relative h-500 w-full overflow-hidden rounded-[12px_12px_0_0] md:h-240"
          >
            <img
              :src="item.image"
              alt="about-1"
              class="h-full w-full object-cover"
            >
          </div>
          <div
            class="absolute left-15 top-210 z-2 hidden h-88 w-88 items-center justify-center rounded-full bg-#FFFFFF transition-all duration-200 md:flex"
            style="box-shadow: 0px 50px 60px -10px rgba(0, 0, 0, 0.08)"
          >
            <img
              src="@/assets/images/home/icon-quote.svg"
              alt="quote"
              class="h-auto w-35%"
            >
          </div>
          <div
            class="relative h-700 w-full rounded-[0px_0px_12px_12px] bg-white px-20 py-45 transition-all duration-400 md:h-340"
          >
            <div
              class="text-semibold mb-30 text-55 text-#1B152B md:mb-10 md:text-24"
            >
              {{ item.title }}
            </div>
            <div
              class="whitespace-pre-wrap text-40 text-[rgba(27,21,43,0.5)] lh-55 md:text-15 md:lh-20"
            >
              {{ item.desc }}
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
      <div
        v-if="false"
        class="mt-50 flex items-center justify-center gap-50 md:mt-30"
      >
        <img
          :src="ArrowRightActive"
          alt="arrow"
          class="z-10 h-120 w-auto rotate-180 cursor-pointer md:h-64"
          @click="changeIndex(-1)"
        >
        <img
          :src="ArrowRightActive"
          alt="arrow"
          class="z-10 h-120 w-auto cursor-pointer md:h-64"
          @click="changeIndex(1)"
        >
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped>
.about-section {
  background: url('@/assets/images/home/bg-about.webp') no-repeat center bottom / cover;
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
