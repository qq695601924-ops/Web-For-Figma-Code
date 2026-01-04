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
    <div class="area h-600 flex justify-between">
      <img
        src="@/assets/images/home/post-question.webp"
        alt="question"
        class="w-auto h-593"
      />
      <div class="w-632">
        <div class="text-48 font-bold lh-55 mb-40">
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
          class="h-80 overflow-hidden transition-all duration-200 cursor-pointer"
          :class="{
            '!h-215': item.open && index === 0,
            '!h-155': item.open && index === 1,
            '!h-285': item.open && index === 2,
            '!h-205': item.open && index === 3,
          }"
          @click="changeActiveIndex(index)"
        >
          <div class="text-24 font-bold lh-80 relative">
            {{ item.title }}
            <img
              v-if="item.open"
              src="@/assets/images/home/icon-question-close.svg"
              alt="arrow-down"
              class="w-auto h-32 absolute right-0 top-1/2 -translate-y-1/2"
            />
            <img
              v-else
              src="@/assets/images/home/icon-question-open.svg"
              alt="arrow-down"
              class="w-auto h-32 absolute right-0 top-1/2 -translate-y-1/2"
            />
          </div>
          <div
            class="text-14 lh-23 text-[rgba(27,21,43,0.5)] pb-20"
            v-html="item.desc"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>
