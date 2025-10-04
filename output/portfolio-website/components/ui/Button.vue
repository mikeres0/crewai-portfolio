<template>
  <button
    :type="type"
    :class="[baseClass, variantClass, sizeClass, { 'opacity-50 cursor-not-allowed': disabled }]"
    :disabled="disabled"
    @click="onClick"
    :aria-label="ariaLabel"
    v-bind="$attrs"
  >
    <span class="flex items-center justify-center">
      <slot />
      <span v-if="loading" class="ml-2 animate-spin rounded-full w-4 h-4 border-2 border-electric border-t-transparent"></span>
    </span>
  </button>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'glass' | 'danger';
  size?: 'lg' | 'md' | 'sm';
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
  loading?: boolean;
  ariaLabel?: string;
}

const props = defineProps<ButtonProps>();
const emit = defineEmits<{ (e: 'click', event: MouseEvent): void }>();

function onClick(event: MouseEvent) {
  if (!props.disabled && !props.loading) emit('click', event);
}

const baseClass = 'font-heading rounded-btn transition-transform duration-150 focus:outline-none focus:ring-2 focus:ring-electric focus:ring-offset-2 active:scale-95 min-h-[40px] min-w-[44px] px-6 py-3';
const variantClass = {
  primary: 'bg-gradient-to-r from-electric via-info to-vividpurple text-deepblue shadow-glass glass hover:scale-105 hover:from-info hover:to-electric',
  secondary: 'bg-transparent border-2 border-electric text-electric glass hover:bg-electric hover:text-deepblue',
  glass: 'bg-glass text-crystalwhite shadow-glass glass',
  danger: 'bg-error text-crystalwhite hover:bg-coral',
}[props.variant ?? 'primary'];
const sizeClass = {
  lg: 'text-xl py-4 px-8',
  md: 'text-base py-3 px-6',
  sm: 'text-sm py-2 px-4',
}[props.size ?? 'md'];
</script>
