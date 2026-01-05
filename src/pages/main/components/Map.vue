<template>
  <div
    id="map-section"
    class="map-section h-800 md:block hidden"
    style="scroll-margin-top: 160px"
  >
    <div class="area">
      <div class="card left-113 top-280" data-bottom-center>🇲🇽 Mexico</div>
      <div class="card left-203 top-370" data-bottom-center>🇨🇴 Colombia</div>
      <div class="card left-315 top-440" data-bottom-center>🇧🇷 Brazil</div>
      <div class="card left-515 top-430" data-top-center>🇳🇬 Nigeria</div>
      <div class="card left-648 top-483" data-top-center>🇰🇪 Kenya</div>
      <div class="card left-808 top-485" data-top-right>🇮🇩 Indonesia</div>
      <div class="card right-10 top-420" data-top-left>🇵🇭 Philippines</div>
      <div class="card right-10 top-490" data-bottom-left>🇦🇺 Australia</div>
      <div class="card right-370 top-250" data-bottom-right>🇵🇰 Pakistan</div>
      <div class="card right-415 top-350 flex items-center justify-center" data-top-right>
        <img src="@/assets/images/home/gcc.svg" alt="GCC" class="w-auto h-25 mr-4" /> GCC
      </div>
      <div class="card right-142 top-270" data-bottom-left>🇧🇩 Bangladesh</div>
      <div class="card right-262 top-370" data-top-left>🇮🇳 India</div>
      <div class="card right-162 top-195" data-bottom-right>🇰🇷 Korea</div>
      <div class="card right-32 top-215" data-bottom-left>🇯🇵 Japan</div>
      <div
        class="card right-72 top-315 flex items-center justify-center"
        data-bottom-left
      >
        <img src="@/assets/images/home/tw.webp" alt="tw" class="w-auto h-25 mr-4" />
        Taiwan
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

  &:hover {
    --card-theme-bg: hsla(162, 64%, 56%, 1);
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
