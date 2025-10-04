<template>
  <span
    :class="['inline-flex items-center px-3 py-1 rounded-full glass font-body text-xs font-semibold shadow-glass', colorClass]"
    :aria-label="ariaLabel"
  >
    <slot />
  </span>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
interface BadgeProps {
  color?: 'primary' | 'secondary' | 'success' | 'error' | 'info';
  ariaLabel?: string;
}
const props = defineProps<BadgeProps>();
const colorClass = {
  primary: 'bg-electric text-deepblue',
  secondary: 'bg-vividpurple text-crystalwhite',
  success: 'bg-emerald text-crystalwhite',
  error: 'bg-error text-crystalwhite',
  info: 'bg-info text-deepblue',
}[props.color ?? 'primary'];
</script>
