<template>
  <div class="flex flex-col mb-4">
    <label :for="id" class="mb-2 font-body text-sm font-medium text-crystalwhite">{{ label }}</label>
    <textarea
      :id="id"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      :aria-invalid="!!error"
      :aria-describedby="error ? id + '-error' : undefined"
      class="glass bg-glass neumorph border-none rounded-btn py-3 px-4 text-crystalwhite placeholder:text-b3b9c9 focus:ring-2 focus:ring-electric outline-none transition-all duration-150 min-h-[120px] resize-none"
      @input="$emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
      v-bind="$attrs"
    />
    <span v-if="error" :id="id + '-error'" class="text-error text-xs mt-1">{{ error }}</span>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';
interface TextareaProps {
  id: string;
  label: string;
  modelValue: string;
  placeholder?: string;
  disabled?: boolean;
  error?: string;
}
const props = defineProps<TextareaProps>();
const emit = defineEmits(['update:modelValue']);
</script>
