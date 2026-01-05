<script setup lang="ts">
import { computed } from "vue";
import familyImg from "@/assets/images/partners/family.svg";
import jiekouImg from "@/assets/images/partners/jiekou.svg";
import paytaImg from "@/assets/images/partners/payta.svg";
import googlePayImg from "@/assets/images/partners/googlePay.svg";
import expressImg from "@/assets/images/partners/express.svg";
import dinersImg from "@/assets/images/partners/diners.svg";
import masterImg from "@/assets/images/partners/master.svg";
import visaImg from "@/assets/images/partners/visa.svg";
import jcbImg from "@/assets/images/partners/jcb.svg";
import bpayImg from "@/assets/images/partners/bpay.svg";
import payIdImg from "@/assets/images/partners/payId.svg";
import payImg from "@/assets/images/partners/pay.svg";
import kbImg from "@/assets/images/partners/kb.svg";
import toassImg from "@/assets/images/partners/toass.svg";
import vaImg from "@/assets/images/partners/va.svg";
import paypayImg from "@/assets/images/partners/paypay.svg";
import sevenImg from "@/assets/images/partners/seven.svg";
import paytmImg from "@/assets/images/partners/paytm.svg";
import phoneImg from "@/assets/images/partners/phone.svg";
import upiImg from "@/assets/images/partners/upi.svg";

const partners = [
  { name: "family", image: familyImg },
  { name: "jiekou", image: jiekouImg },
  { name: "payta", image: paytaImg },
  { name: "googlePay", image: googlePayImg },
  { name: "express", image: expressImg },
  { name: "diners", image: dinersImg },
  { name: "master", image: masterImg },
  { name: "visa", image: visaImg },
  { name: "jcb", image: jcbImg },
  { name: "bpay", image: bpayImg },
  { name: "payId", image: payIdImg },
  { name: "pay", image: payImg },
  { name: "kb", image: kbImg },
  { name: "toass", image: toassImg },
  { name: "va", image: vaImg },
  { name: "paypay", image: paypayImg },
  { name: "seven", image: sevenImg },
  { name: "paytm", image: paytmImg },
  { name: "phone", image: phoneImg },
  { name: "upi", image: upiImg },
];

// 将数组按每行分组
const partnerLines = computed(() => {
  const lines: typeof partners[] = [];
  const itemsPerLine = [4, 5, 4, 5, 3]; // 每行的数量
  let index = 0;

  for (const count of itemsPerLine) {
    lines.push(partners.slice(index, index + count));
    index += count;
  }

  return lines;
});
</script>

<template>
  <div class="partners-section pb-100">
    <div class="area md:px-0 px-50">
      <div class="md:text-48 text-88 font-bold mb-20 text-center">
        Payment Methods & Partners
      </div>
      <div
        class="md:text-20 text-44 text-[rgba(27,21,43,0.6)] text-center md:mb-40 mb-70"
      >
        Trusted by leading financial institutions and local wallets worldwide.
      </div>
      <div
        v-for="(line, lineIndex) in partnerLines"
        :key="lineIndex"
        class="justify-center items-center gap-50 md:flex hidden"
        :class="{ 'mb-40': lineIndex < partnerLines.length - 1 }"
      >
        <div v-for="partner in line" :key="partner.name" class="partner-card">
          <img :src="partner.image" :alt="partner.name" />
        </div>
      </div>
      <div class="md:hidden grid grid-cols-4 gap-50">
        <div v-for="partner in partners" :key="partner.name" class="partner-card">
          <img :src="partner.image" :alt="partner.name" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
.partner-card {
  width: 200px;
  height: 82px;
  background-color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 1px 4px 12px 0px rgba(0, 0, 0, 0.08);
  img {
    width: auto;
    height: 40px;
  }
}

@media (max-width: 768px) {
  .partner-card {
    width: auto;
    height: 250px;
    img {
      height: 90px;
    }
  }
}
</style>
