<script setup lang="ts">
const questionList = reactive([
  {
    title: "Single Aggregated Account Balance",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        As a Master Merchant, Vexora prefers to manage deposit (pay-in) and disbursement (pay-out) for all merchants through a single aggregated account balance.
      </li>
      <li>
        As Vexora does not maintain a local bank account, the local payment provider will hold funds on our behalf to continuously support deposit and disbursement activities until a settlement request is initiated.
      </li>
    </ul>
      `,
    open: true,
  },
  {
    title: "Fee Netting (Preferred)",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        Service fees are netted at the transaction level, allowing fees to be deducted automatically from each transaction rather than settled separately.
      </li>
    </ul>
    `,
    open: false,
  },
  {
    title: "No Automatic Settlement",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        Vexora is required to maintain a minimum balance to ensure sufficient liquidity for customer disbursements.
      </li>
      <li>
        As transaction volumes increase, the required maintained balance will scale accordingly.
      </li>
      <li>
       For this reason, settlements are conducted on a request basis only, rather than automatically.
- Settlement frequency may range from every few days to once per week, depending on the maintained balance level.
- A dedicated finance manager will be assigned by Vexora to initiate and manage settlement requests.
      </li>
    </ul>
    `,
    open: false,
  },
  {
    title: "Dashboard Access",
    desc: `
    <ul class="list-disc list-outside pl-1em">
      <li>
        Access to a dashboard is required to:
- View transaction records
- Monitor account balances in real time
      </li>
      <li>
 Please note that with some providers, account balance updates may take several hours up to one business day after settlement processing is completed.
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
          Vexora's Account with Local Provider
        </div>
        <div
          v-for="(item, index) in questionList"
          :key="item.title"
          style="border-top: 1px solid #e5e5e5"
          :style="{
            borderBottom:
              index === questionList.length - 1 ? '1px solid #e5e5e5' : 'none',
          }"
          class="md:h-80 h-150 overflow-hidden transition-all duration-200 cursor-pointer"
          :class="{
            '!md:h-215 h-600': item.open && index === 0,
            '!md:h-155 h-370': item.open && index === 1,
            '!md:h-285 h-750': item.open && index === 2,
            '!md:h-205 h-480': item.open && index === 3,
          }"
          @click="changeActiveIndex(index)"
        >
          <div class="md:text-24 text-50 font-bold md:lh-80 lh-150 relative">
            {{ item.title }}
            <img
              v-if="item.open"
              src="@/assets/images/home/icon-question-close.svg"
              alt="arrow-down"
              class="w-auto md:h-32 h-60 absolute right-0 top-1/2 -translate-y-1/2"
            />
            <img
              v-else
              src="@/assets/images/home/icon-question-open.svg"
              alt="arrow-down"
              class="w-auto md:h-32 h-60 absolute right-0 top-1/2 -translate-y-1/2"
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
