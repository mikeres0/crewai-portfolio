<template>
  <div :class="[$themeClass]" id="__nuxt">
    <a href="#main-content" class="sr-only focus:not-sr-only absolute top-2 left-2 z-50 bg-electric text-deepblue rounded-btn px-4 py-2 font-heading">Skip to content</a>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
    <div id="global-loader" aria-live="polite" aria-busy="false" v-if="isLoading" class="fixed top-0 left-0 w-full h-1 z-50">
      <div class="bg-gradient-to-r from-electric via-vividpurple to-cobalt animate-loader h-full w-full"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useTheme } from '@/composables/useTheme';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const { themeClass } = useTheme();
const isLoading = ref(false);
const router = useRouter();

router.beforeEach(() => {
  isLoading.value = true;
});
router.afterEach(() => {
  isLoading.value = false;
});
</script>

<style>
.animate-loader {
  animation: loader 1.5s cubic-bezier(0.4,0.0,0.2,1) infinite;
}
@keyframes loader {
  0% { transform: translateX(-100%); opacity: 0; }
  50% { transform: translateX(0); opacity: 1; }
  100% { transform: translateX(100%); opacity: 0; }
}
</style>
