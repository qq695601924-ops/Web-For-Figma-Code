<script setup lang="ts">
import { useLanguage } from "@/composables/language";
import { useI18n } from "vue-i18n";

const { language } = useLanguage();
const { t } = useI18n();

const questionList = reactive([
  {
    title: computed(() => t('question.securityFirst.title')),
    desc: computed(() => `
    <ul class="list-disc list-outside pl-1em">
      <li>
${t('question.securityFirst.desc')}</li>
    </ul>
      `),
    open: true,
  },
  {
    title: computed(() => t('question.riskAwareness.title')),
    desc: computed(() => `
    <ul class="list-disc list-outside pl-1em">
      <li>
        ${t('question.riskAwareness.desc')}
      </li>
    </ul>
    `),
    open: false,
  },
  {
    title: computed(() => t('question.trustTechnology.title')),
    desc: computed(() => `
    <ul class="list-disc list-outside pl-1em">
      <li>
        ${t('question.trustTechnology.desc')}
      </li>
    </ul>
    `),
    open: false,
  },
]);
const changeActiveIndex = (index: number) => {
  questionList.forEach((item, i) => {
    if (i !== index) {
      item.open = false;
    } else {
      item.open = true;
    }
  });
};
</script>

<template>
  <div id="question-section" class="question-section py-150">
    <div class="area md:h-600 h-auto flex justify-between md:px-0 px-60">
      <img
        src="@/assets/images/home/post-question.webp"
        alt="question"
        class="w-auto h-593 md:block hidden"
      />
      <div class="md:w-632 w-full">
        <div class="md:text-48 text-88 font-bold md:lh-55 lh-100 md:mb-40 mb-70">
          {{ t('question.title') }}
        </div>
        <div
          v-for="(item, index) in questionList"
          :key="index"
          style="border-top: 1px solid #e5e5e5"
          :style="{
            borderBottom:
              index === questionList.length - 1 ? '1px solid #e5e5e5' : 'none',
          }"
          class="md:h-80 h-150 overflow-hidden transition-all duration-200 cursor-pointer"
          :class="{
            '!md:h-180 h-450': item.open && [0, 1, 2].includes(index),
          }"
          @click="changeActiveIndex(index)"
        >
          <div
            class="md:text-24 text-50 font-bold md:lh-80 lh-150 relative"
            :class="{ 'text-[var(--primary-color)]': item.open }"
          >
            {{ item.title }}
            <img
              v-if="!item.open"
              src="@/assets/images/home/icon-question-close.svg"
              alt="arrow-down"
              class="w-auto md:h-32 h-60 absolute top-1/2 -translate-y-1/2"
              :class="language === 'ur' ? 'left-0' : 'right-0'"
            />
            <img
              v-else
              src="@/assets/images/home/icon-question-open.svg"
              alt="arrow-down"
              class="w-auto md:h-32 h-60 absolute top-1/2 -translate-y-1/2"
              :class="language === 'ur' ? 'left-0' : 'right-0'"
            />
          </div>
          <div
            class="md:text-14 text-44 md:lh-23 lh-55 text-[rgba(27,21,43,0.5)] pb-20"
            v-html="item.desc"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>
