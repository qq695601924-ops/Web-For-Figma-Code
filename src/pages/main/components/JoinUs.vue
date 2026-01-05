<script setup lang="ts">
import { useToast } from "vue-toast-notification";

const toast = useToast();
const step = ["Contact Us", "Sign contract", "Integration", "Product release"];

const form = ref({
  name: "",
  email: "",
  phone: "",
  companyName: "",
  companyWebsite: "",
  message: "",
});

const handleSubmit = () => {
  // 验证表单字段
  if (
    !form.value.name.trim() ||
    !form.value.email.trim() ||
    !form.value.phone.trim() ||
    !form.value.companyName.trim() ||
    !form.value.companyWebsite.trim() ||
    !form.value.message.trim()
  ) {
    toast.error("Please complete all fields", {
      position: "top-right",
    });
    return;
  }

  // 清空表单
  form.value = {
    name: "",
    email: "",
    phone: "",
    companyName: "",
    companyWebsite: "",
    message: "",
  };

  // 显示成功提示
  toast.success("Message sent successfully!", {
    position: "top-right",
  });
};
</script>

<template>
  <div id="contact-section" class="py-150">
    <div
      class="area md:h-666 h-auto rounded-16 bg-#F4FBF9 md:px-40 px-50 md:py-40 py-100 md:flex blockjustify-between items-center"
    >
      <div class="md:w-500 w-full flex flex-col gap-30 md:mb-0 mb-50">
        <div class="md:text-48 text-88 font-semibold">Ready to Join Us?</div>
        <div class="md:text-15 text-44 md:lh-24 lh-50 text-[rgba(27,21,43,0.6)]">
          Join thousands of businesses that trust Vexora for their payment and recharge
          needs.
        </div>
        <div class="md:flex grid grid-cols-2 flex-col gap-20 step-wrapper">
          <div
            v-for="(item, index) in step"
            :key="item"
            class="md:h-48 h-88 relative md:lh-48 lh-88"
          >
            <div
              class="bg-#F4FBF9 md:w-48 w-88 md:h-48 h-88 rounded-full md:text-24 text-48 text-#47D7AC flex items-center justify-center absolute left-0 top-50% -translate-y-50%"
              style="border: 2px solid #47d7ac"
            >
              {{ index + 1 }}
            </div>
            <div class="md:text-20 text-46 md:pl-60 pl-120">
              {{ item }}
            </div>
          </div>
        </div>
      </div>
      <div
        class="md:w-567 w-full md:h-586 h-auto bg-[rgba(71,215,172,0.1)] rounded-16 px-40 py-40"
      >
        <div class="flex items-center justify-between mb-24">
          <input
            type="text"
            placeholder="Name"
            class="custom-input md:w-230 w-48% md:h-54 h-120 rounded-8 bg-#FFFFFF border-none px-20"
            v-model="form.name"
          />
          <input
            type="text"
            placeholder="Email"
            class="custom-input md:w-230 w-48% md:h-54 h-120 rounded-8 bg-#FFFFFF border-none px-20"
            v-model="form.email"
          />
        </div>
        <div class="mb-24">
          <input
            type="text"
            placeholder="Phone"
            class="custom-input w-full md:h-54 h-120 rounded-8 bg-#FFFFFF border-none px-20"
            v-model="form.phone"
          />
        </div>
        <div class="mb-24">
          <input
            type="text"
            placeholder="Company Name"
            class="custom-input w-full md:h-54 h-120 rounded-8 bg-#FFFFFF border-none px-20"
            v-model="form.companyName"
          />
        </div>
        <div class="mb-24">
          <input
            type="text"
            placeholder="Company Website / Product Link"
            class="custom-input w-full md:h-54 h-120 rounded-8 bg-#FFFFFF border-none px-20"
            v-model="form.companyWebsite"
          />
        </div>
        <div class="mb-24">
          <textarea
            placeholder="Message"
            class="custom-input w-full md:h-100 h-120 rounded-8 bg-#FFFFFF border-none px-20 py-20 resize-none"
            v-model="form.message"
          ></textarea>
        </div>
        <div
          class="hover-scale w-full md:h-60 h-120 rounded-8 bg-#47D7AC flex items-center justify-center md:text-20 text-45 text-#211551 font-semibold cursor-pointer"
          @click="handleSubmit"
        >
          Contact Us
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped>
.step-wrapper {
  position: relative;
  &::before {
    content: "";
    position: absolute;
    left: 24px;
    top: 50%;
    transform: translateY(-50%);
    width: 2px;
    height: 100%;
    background: #47d7ac;
  }
}
.custom-input {
  &::placeholder {
    color: rgba(40, 37, 29, 0.5);
  }
  &:focus {
    outline: none;
  }
}

@media (max-width: 768px) {
  .step-wrapper {
    &::before {
      display: none;
    }
  }
}
</style>

<style lang="less">
@media (max-width: 768px) {
  .v-toast__item .v-toast__icon {
    width: 70px;
    height: 70px;
    img {
      width: 100%;
      height: 100%;
    }
  }
  .v-toast__item {
    min-height: 3em;
  }
  .v-toast__text {
    padding: 0px 45px !important;
  }
}
</style>
