<template>
  <div
    id="map-section"
    class="map-section h-800 md:block hidden mt-150"
    style="scroll-margin-top: 160px"
  >
    <div class="area relative h-full">
      <div class="card left-113 top-280" data-bottom-center>
        <div class="flex items-center">
          <img src="@/assets/images/home/mexico.webp" alt="mx" class="w-auto h-25 mr-4" />
          Mexico
        </div>
      </div>
      <div class="card left-203 top-370" data-bottom-center>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/colombia.webp"
            alt="co"
            class="w-auto h-25 mr-4"
          />
          Colombia
        </div>
      </div>
      <div class="card left-315 top-440" data-bottom-center>
        <div class="flex items-center">
          <img src="@/assets/images/home/brazil.webp" alt="br" class="w-auto h-25 mr-4" />
          Brazil
        </div>
      </div>
      <div class="card left-515 top-430" data-top-center>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/nigeria.webp"
            alt="ng"
            class="w-auto h-25 mr-4"
          />
          Nigeria
        </div>
      </div>
      <div class="card left-648 top-483" data-top-center>
        <div class="flex items-center">
          <img src="@/assets/images/home/kenya.webp" alt="ke" class="w-auto h-25 mr-4" />
          Kenya
        </div>
      </div>
      <div class="card left-808 top-485" data-top-right>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/indonesia.webp"
            alt="id"
            class="w-auto h-25 mr-4"
          />
          Indonesia
        </div>
      </div>
      <div class="card right-10 top-420" data-top-left>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/philippines.webp"
            alt="ph"
            class="w-auto h-25 mr-4"
          />
          Philippines
        </div>
      </div>
      <div class="card card-aus left-1035 bottom-245" data-bottom-left>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/australia.webp"
            alt="au"
            class="w-auto h-25 mr-4"
          />
          Australia
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          Trusted Local Acquiring in a High-Compliance Market
        </div>
      </div>
      <div class="card right-370 top-250" data-bottom-right>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/pakistan.webp"
            alt="pk"
            class="w-auto h-25 mr-4"
          />
          Pakistan
        </div>
      </div>
      <div class="card card-gcc right-415 top-350" data-top-right>
        <div class="flex items-center">
          <img src="@/assets/images/home/gcc.svg" alt="GCC" class="w-auto h-25 mr-4" />
          GCC
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          Enable GCC Card Payments with Confidence
        </div>
      </div>
      <div class="card right-142 top-270" data-bottom-left>
        <div class="flex items-center">
          <img
            src="@/assets/images/home/bangladesh.webp"
            alt="bd"
            class="w-auto h-25 mr-4"
          />
          Bangladesh
        </div>
      </div>
      <div class="card card-ind left-832 top-370" data-top-left>
        <div class="flex items-center">
          <img src="@/assets/images/home/india.webp" alt="in" class="w-auto h-25 mr-4" />
          India
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          UPI, Cards, and Scale—Handled Locally
        </div>
      </div>
      <div class="card card-korea right-162 bottom-535" data-bottom-right>
        <div class="flex items-center">
          <img src="@/assets/images/home/korea.webp" alt="kr" class="w-auto h-25 mr-4" />
          Korea
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          Advanced Card & Local Payments for a Tech-Driven Market
        </div>
      </div>
      <div class="card card-jp left-1032 bottom-515" data-bottom-left>
        <div class="flex items-center">
          <img src="@/assets/images/home/japan.webp" alt="jp" class="w-auto h-25 mr-4" />
          Japan
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          Precision Payments for a Complex Ecosystem
        </div>
      </div>
      <div class="card card-tw left-989 bottom-425" data-bottom-left>
        <div class="flex items-center">
          <img src="@/assets/images/home/tw.webp" alt="tw" class="w-auto h-25 mr-4" />
          Taiwan
        </div>
        <div class="text-16 text-[rgba(27,21,43,0.4)] lh-24 font-400 desc">
          Fully Localized Acquiring for a Mature Digital Market
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped>
.map-section {
  background: url("@/assets/images/home/bg-map.svg") no-repeat center top / auto 100%;
}
.card {
  --card-theme-bg: hsla(0, 0%, 100%, 0.7);
  background: var(--card-theme-bg);
  height: 55px;
  position: absolute;
  line-height: 55px;
  text-align: center;
  font-size: 21px;
  border-radius: 10px;
  font-weight: bold;
  padding: 0 15px;
  box-shadow: 0px 10px 20px 10px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: all 0.3s ease;
  .desc {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    user-select: none;
    transition: all 0s;
  }
  &.card-jp,
  &.card-gcc,
  &.card-tw,
  &.card-aus,
  &.card-ind,
  &.card-korea {
    width: 130px;
    text-align: left;
  }
  &.card-aus {
    width: 160px;
  }
  &:hover {
    --card-theme-bg: hsla(162, 64%, 56%, 1);
    &.card-jp,
    &.card-gcc,
    &.card-tw,
    &.card-aus,
    &.card-ind,
    &.card-korea {
      width: 250px;
      --card-theme-bg: hsla(0, 0%, 100%, 1);
      height: 120px;
      z-index: 99;
      .desc {
        opacity: 1;
        visibility: visible;
        transition: all 0.18s ease 0.18s;
      }
    }
    &.card-korea {
      width: 320px;
    }
  }
  &::before {
    content: "";
    position: absolute;
    transition: all 0.3s ease;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
  }
  // 下局中的三角形
  &[data-bottom-center]::before {
    bottom: -9px;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid var(--card-theme-bg);
  }
  &[data-bottom-left]::before {
    bottom: -9px;
    left: 20px;
    right: auto;
    transform: translateX(0);
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid var(--card-theme-bg);
  }
  &[data-bottom-right]::before {
    bottom: -9px;
    right: 20px;
    left: auto;
    transform: translateX(0);
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid var(--card-theme-bg);
  }
  &[data-top-center]::before {
    top: -9px;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-bottom: 10px solid var(--card-theme-bg);
  }
  &[data-top-right]::before {
    top: -9px;
    right: 20px;
    left: auto;
    transform: translateX(0);
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-bottom: 10px solid var(--card-theme-bg);
  }
  &[data-top-left]::before {
    top: -9px;
    left: 20px;
    right: auto;
    transform: translateX(0);
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-bottom: 10px solid var(--card-theme-bg);
  }
}
</style>
