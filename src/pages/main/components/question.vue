<script setup lang="ts">
const questionList = reactive([
  {
    title: "Security-First Architecture",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
Optivolve Digital is designed with security as a foundational principle. Our platform applies structured controls and best-practice approaches to help safeguard transaction data throughout its lifecycle.</li>
    </ul>
      `,
    open: true,
  },
  {
    title: "Risk Awareness and Prevention",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        We focus on reducing operational and transaction-related risks through continuous monitoring, system safeguards, and thoughtful design — helping businesses operate with greater stability and confidence.
      </li>
    </ul>
    `,
    open: false,
  },
  {
    title: "Trust Through Responsible Technology",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        By prioritizing data protection and transparent processes, Optivolve Digital supports responsible transaction handling and helps businesses build long-term trust with their users.
      </li>
    </ul>
    `,
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
          Security Built Into Every Transaction
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
              class="w-auto md:h-32 h-60 absolute top-1/2 -translate-y-1/2 right-0"
            />
            <img
              v-else
              src="@/assets/images/home/icon-question-open.svg"
              alt="arrow-down"
              class="w-auto md:h-32 h-60 absolute top-1/2 -translate-y-1/2 right-0"
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
