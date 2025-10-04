<template>
  <div class="min-h-screen flex flex-col bg-darkbg text-crystalwhite">
    <Header />
    <main class="flex-1" id="main-content"><slot /></main>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/layout/Header.vue';
import Footer from '@/components/layout/Footer.vue';
</script>
