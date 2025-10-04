<template>
  <footer class="glass bg-glass backdrop-blur-glass shadow-glass w-full py-8 px-8 md:px-16 flex flex-col md:flex-row items-center justify-between text-b3b9c9 text-sm mt-8">
    <div class="flex items-center gap-4 mb-4 md:mb-0">
      <span class="font-heading font-bold text-electric">C# Portfolio</span>
      <span aria-hidden="true">|</span>
      <span>© {{ year }} Your Name</span>
    </div>
    <div class="flex gap-6">
      <a href="mailto:your.email@example.com" aria-label="Email" class="hover:text-electric focus:outline-none focus:ring-2 ring-electric rounded-btn transition">
        <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12h2a2 2 0 012 2v6a2 2 0 01-2 2H6a2 2 0 01-2-2v-6a2 2 0 012-2h2" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 16v-4m0 0l-3 3m3-3l3 3" /></svg>
      </a>
      <a href="https://linkedin.com/in/yourprofile" aria-label="LinkedIn" target="_blank" rel="noopener" class="hover:text-electric focus:outline-none focus:ring-2 ring-electric rounded-btn transition">
        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M16 8a6 6 0 016 6v6a2 2 0 01-2 2h-4a2 2 0 01-2-2v-6a2 2 0 012-2z" /><circle cx="8" cy="8" r="3" /><rect width="6" height="12" x="2" y="10" rx="2" /></svg>
      </a>
      <a href="https://github.com/yourprofile" aria-label="GitHub" target="_blank" rel="noopener" class="hover:text-electric focus:outline-none focus:ring-2 ring-electric rounded-btn transition">
        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.486 2 12c0 4.418 2.865 8.167 6.839 9.489.5.091.682-.217.682-.482 0-.237-.009-.868-.014-1.703-2.782.605-3.369-1.342-3.369-1.342-.454-1.157-1.11-1.465-1.11-1.465-.908-.62.069-.608.069-.608 1.003.071 1.531 1.031 1.531 1.031.892 1.527 2.341 1.087 2.91.832.091-.646.35-1.087.636-1.338-2.221-.253-4.555-1.112-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.271.097-2.648 0 0 .84-.27 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.338 1.909-1.295 2.748-1.025 2.748-1.025.545 1.377.202 2.395.1 2.648.64.7 1.028 1.595 1.028 2.688 0 3.848-2.337 4.695-4.566 4.943.36.309.679.919.679 1.854 0 1.338-.013 2.421-.013 2.749 0 .268.18.579.688.481C19.138 20.164 22 16.418 22 12c0-5.514-4.477-10-10-10z"/></svg>
      </a>
    </div>
    <div class="mt-4 md:mt-0 text-xs">
      <span class="mr-2">WCAG 2.1 AA Accessible</span>
      <span aria-hidden="true">|</span>
      <span>Crafted with Nuxt 3, Tailwind, GSAP</span>
    </div>
  </footer>
</template>

<script setup lang="ts">
const year = new Date().getFullYear();
</script>
