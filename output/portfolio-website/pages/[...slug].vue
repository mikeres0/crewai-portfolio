<template>
  <section class="flex flex-col items-center justify-center min-h-screen bg-darkbg text-crystalwhite">
    <div class="glass p-12 rounded-card shadow-glass flex flex-col items-center animate-fadein">
      <h1 class="font-heading text-6xl text-electric mb-4" aria-label="404 Page Not Found">404</h1>
      <h2 class="text-2xl font-semibold mb-3">Page Not Found</h2>
      <p class="mb-6 text-lg text-center max-w-lg">
        Sorry, the page you’re looking for doesn’t exist. Let’s get you back to the homepage and keep exploring C# mastery!
      </p>
      <Button @click="$router.push('/')" aria-label="Go to home" variant="primary">Return Home</Button>
    </div>
  </section>
</template>

<script setup lang="ts">
import Button from '@/components/ui/Button.vue';
</script>

<style scoped>
.animate-fadein {
  animation: fadein 0.5s cubic-bezier(0.4,0.0,0.2,1);
}
@keyframes fadein {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
