<script setup lang="ts"></script>

<template>
  <div class="business-section py-100">
    <div class="area md:px-0 px-100">
      <img
        src="@/assets/images/home/post-business.svg"
        alt="business-1"
        class="w-auto h-800 absolute -left-80 -top-250 md:block hidden"
      />
      <ul
        class="list-decimal list-outside pl-15 md:w-535 w-full md:text-16 text-40 md:lh-24 lh-50 text-[rgba(27,21,43,0.6)] ml-auto"
      >
        <li class="md:mb-15 mb-50">
          Ideally we will always want to have a "master merchant" business model where
          Vexora will act as a single merchant to local provider and our merchants will
          connect via us.
        </li>
        <li class="md:mb-15 mb-50">
          Any agreement and settlement arrangement is directly between Vexora and Local
          Partner
          <ul class="list-disc list-outside -pl-15">
            <li>
              Vexora will have its own agreement and settlement arrangement with our
              merchants
            </li>
            <li>
              Any communication between our merchants and Local Partner should go through
              Vexora
            </li>
          </ul>
        </li>
        <li class="md:mb-15 mb-100">
          Local Partner give us the "buy rate” and we will add on our margin and offer the
          "sell rate” to our merchants.
          <ul class="list-disc list-outside -pl-15 text-#8A69FF">
            <li>Example: X% (buy rate)+ Y% (margin)= z% (sell rate)</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>
