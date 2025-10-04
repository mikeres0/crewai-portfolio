<template>
  <div
    :class="['glass rounded-card shadow-glass p-8 transition-transform duration-200 will-change-transform', { 'hover:scale-105 hover:shadow-xl': hoverable } ]"
    role="region"
    :aria-label="ariaLabel"
  >
    <slot />
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
interface CardProps {
  hoverable?: boolean;
  ariaLabel?: string;
}
const props = defineProps<CardProps>();
</script>
