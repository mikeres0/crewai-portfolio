<template>
  <div class="fixed inset-0 z-50 bg-darkbg bg-opacity-80 flex items-end md:items-center justify-end">
    <nav class="glass bg-glass backdrop-blur-glass shadow-glass w-full max-w-xs p-8 flex flex-col gap-6 rounded-l-card animate-slidein" tabindex="0" aria-label="Mobile navigation menu">
      <button @click="$emit('close')" aria-label="Close menu" class="self-end text-crystalwhite mb-4 focus:outline-none focus:ring-2 ring-electric rounded-btn">
        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
      <NuxtLink to="/" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">Home</NuxtLink>
      <NuxtLink to="#about" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">About</NuxtLink>
      <NuxtLink to="#skills" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">Skills</NuxtLink>
      <NuxtLink to="#experience" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">Experience</NuxtLink>
      <NuxtLink to="#projects" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">Projects</NuxtLink>
      <NuxtLink to="#contact" @click="$emit('close')" class="font-heading text-lg px-3 py-2 rounded-btn focus:outline-none focus:ring-2 ring-electric hover:text-electric">Contact</NuxtLink>
      <Button variant="primary" size="lg" class="mt-6 w-full" aria-label="Contact" @click="$emit('close'); $router.push('#contact')">Contact</Button>
    </nav>
  </div>
</template>

<script setup lang="ts">
import Button from '@/components/ui/Button.vue';
</script>

<style scoped>
.animate-slidein {
  animation: slidein 0.35s cubic-bezier(0.4,0.0,0.2,1);
}
@keyframes slidein {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}
</style>
