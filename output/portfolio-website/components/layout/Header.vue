<template>
  <header class="sticky top-0 z-40 glass bg-glass backdrop-blur-glass shadow-glass w-full h-20 flex items-center justify-between px-8 md:px-16">
    <div class="flex items-center gap-4">
      <img src="/favicon.ico" alt="C# Developer Logo" class="h-10 w-10 rounded-full" />
      <span class="font-heading text-2xl font-bold text-electric">C# Portfolio</span>
    </div>
    <nav class="hidden md:flex gap-8 font-body text-base">
      <NuxtLink to="/" class="focus:outline-none focus:ring-2 ring-electric px-3 py-1 rounded-btn transition hover:text-electric">Home</NuxtLink>
      <NuxtLink to="#about" class="focus:outline-none px-3 py-1 rounded-btn transition hover:text-electric">About</NuxtLink>
      <NuxtLink to="#skills" class="focus:outline-none px-3 py-1 rounded-btn transition hover:text-electric">Skills</NuxtLink>
      <NuxtLink to="#experience" class="focus:outline-none px-3 py-1 rounded-btn transition hover:text-electric">Experience</NuxtLink>
      <NuxtLink to="#projects" class="focus:outline-none px-3 py-1 rounded-btn transition hover:text-electric">Projects</NuxtLink>
      <NuxtLink to="#contact" class="focus:outline-none px-3 py-1 rounded-btn transition hover:text-electric">Contact</NuxtLink>
    </nav>
    <div class="flex items-center gap-4">
      <Button variant="primary" size="sm" aria-label="Contact" @click="$router.push('#contact')">Contact</Button>
      <button @click="toggleTheme" aria-label="Toggle dark mode" class="focus:outline-none px-3 py-1 rounded-btn transition hover:bg-electric hover:text-deepblue">
        <svg v-if="theme === 'dark'" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12.79A9 9 0 1112.21 3a7 7 0 008.79 9.79z" />
        </svg>
        <svg v-else class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M17.36 17.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M17.36 6.64l1.42-1.42" />
        </svg>
      </button>
      <button class="md:hidden px-3 py-1 rounded-btn" aria-label="Open mobile menu" @click="toggleMenu">
        <svg class="h-6 w-6 text-crystalwhite" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
      </button>
    </div>
    <MobileMenu v-if="menuOpen" @close="menuOpen = false" />
  </header>
</template>

<script setup lang="ts">
import Button from '@/components/ui/Button.vue';
import MobileMenu from '@/components/layout/MobileMenu.vue';
import { ref } from 'vue';
import { useTheme } from '@/composables/useTheme';

const menuOpen = ref(false);
const { theme, toggleTheme } = useTheme();

function toggleMenu() {
  menuOpen.value = !menuOpen.value;
}
</script>
