<template>
  <div
    id="services-section"
    class="services-section md:h-818 h-auto bg-[rgba(147,232,211,0.15)] md:py-0 py-150"
    style="scroll-margin-top: 100px"
  >
    <div
      class="area flex flex-col items-center justify-center md:gap-40 gap-70 h-full md:px-0 px-50"
    >
      <div class="md:text-48 text-88 font-bold text-center md:w-645 w-100%">
        Services Requiredfrom Payment Partner
      </div>
      <div class="grid md:grid-cols-2 grid-cols-1 gap-20 w-full">
        <div
          class="md:h-168 h-auto bg-#FFFFFF border-rd-20 px-25 py-25 flex flex-col justify-between"
          style="box-shadow: 0px 0px 17px 6px rgba(138, 192, 171, 0.15)"
        >
          <div class="flex items-center -mt-10 md:text-24 text-50 font-semibold">
            <img
              src="@/assets/images/home/icon-services-1.svg"
              alt="services-1"
              class="w-auto md:h-76 h-220 -ml-20"
            />
            Deposit (Pay-in)
          </div>
          <div
            class="md:text-16 text-44 md:lh-24 lh-55 text-[rgba(27,21,43,0.5)] md:px-0 px-50 md:pb-0 pb-30"
          >
            Enables customers to deposit funds into merchant accounts in
            <span class="text-#1B152B">local currency</span>.
          </div>
        </div>
        <div
          class="md:h-168 h-auto bg-#FFFFFF border-rd-20 px-25 py-25 flex flex-col justify-between"
          style="box-shadow: 0px 0px 17px 6px rgba(138, 192, 171, 0.15)"
        >
          <div class="flex items-center -mt-10 md:text-24 text-50 font-semibold">
            <img
              src="@/assets/images/home/icon-services-2.svg"
              alt="services-1"
              class="w-auto md:h-76 h-220 -ml-20"
            />
            Disbursement (Pay-out)
          </div>
          <div
            class="md:text-16 text-44 md:lh-24 lh-55 text-[rgba(27,21,43,0.5)] md:px-0 px-50 md:pb-0 pb-30"
          >
            Allows customers to withdraw funds from merchant accounts in
            <span class="text-#1B152B">local currency</span>.
          </div>
        </div>
        <div
          class="md:h-229 h-auto bg-#FFFFFF border-rd-20 px-25 py-20 flex flex-col justify-between"
          style="box-shadow: 0px 0px 17px 6px rgba(138, 192, 171, 0.15)"
        >
          <div class="flex items-center -mt-10 md:text-24 text-50 font-semibold">
            <img
              src="@/assets/images/home/icon-services-3.svg"
              alt="services-1"
              class="w-auto md:h-76 h-220 -ml-20"
            />
            Settlement
          </div>
          <div
            class="md:text-16 text-44 md:lh-24 lh-55 text-[rgba(27,21,43,0.5)] mb-0 -mt-20 md:px-0 px-50 md:pb-0 pb-30"
          >
            Settlement flows from the local payment partner to Vexora, including:
          </div>
          <ul
            class="md:text-14 text-40 md:lh-21 lh-50 text-[rgba(27,21,43,0.5)] list-disc list-outside md:pl-15 pl-80 md:pb-0 pb-30"
          >
            <li>
              <span class="text-#1B152B">Local Settlement</span> - Transfers to our
              remittance partners within the local market
            </li>
            <li>
              <span class="text-#1B152B">Overseas Settlement</span> - Cross-border
              settlements in <span class="text-#1B152B">EUR / USD / USDT</span>
            </li>
          </ul>
        </div>
        <div
          class="md:h-229 h-auto bg-#FFFFFF border-rd-20 px-25 py-25 flex flex-col justify-between"
          style="box-shadow: 0px 0px 17px 6px rgba(138, 192, 171, 0.15)"
        >
          <div class="flex items-center -mt-10 md:text-24 text-50 font-semibold">
            <img
              src="@/assets/images/home/icon-services-4.svg"
              alt="services-1"
              class="w-auto md:h-76 h-220 -ml-20"
            />
            Balance Top-Up
          </div>
          <div
            class="md:text-16 text-44 md:lh-24 lh-55 text-[rgba(27,21,43,0.5)] mb-15 md:px-0 px-50 md:pb-0 pb-30"
          >
            Balance top-up from Vexora to the local payment partner to support liquidity
            needs:
          </div>
          <ul
            class="md:text-14 text-40 md:lh-21 lh-50 text-[rgba(27,21,43,0.5)] list-disc list-outside md:pl-15 pl-80 md:pb-0 pb-30"
          >
            <li>
              <span class="text-#1B152B">Local Top-Up </span>
            </li>
            <li>
              <span class="text-#1B152B">Overseas Top-Up (EUR / USD / USDT)</span>
            </li>
          </ul>
        </div>
      </div>
      <div
        class="md:w-944 w-full md:h-72 h-auto md:py-0 py-50 bg-[#93E8D3] border-rd-8 md:text-16 text-40 md:lh-24 lh-50 text-center flex items-center justify-center px-25"
      >
        In certain scenarios, merchants may require higher disbursement (pay-out) volumes,
        making timely balance top-ups essential to ensure smooth transaction processing.
      </div>
    </div>
  </div>
</template>
