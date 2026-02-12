<template>
  <div>
    <!-- <NavBar /> -->
    <router-view v-slot="{ Component, route }">
      <transition name="scale" mode="out-in">
        <keep-alive>
          <component :is="Component" :key="route.name" />
        </keep-alive>
      </transition>
    </router-view>
    <!-- <Footer /> -->
  </div>
</template>

<style scoped>
.scale-enter-active,
.scale-leave-active {
  transition: all 0.3s ease;
  visibility: visible;
}

.scale-enter-from,
.scale-leave-to {
  opacity: 0;
  visibility: hidden;
  transform: scale(1.05);
}
</style>
