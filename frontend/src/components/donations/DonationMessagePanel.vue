<template>
  <p>
    You can type a small message, or leave it blank.
  </p>
  <Textarea
    v-model="props.data.message"
    placeholder="Thanks for helping me find my pet donkey!"
    autoResize
    rows="5"
    cols="30" />

  <p>
    And you can put in your name, if you're feeling like it.
  </p>
  <InputText
    v-model="props.data.author"
    placeholder="Anonymous" />

</template>

<script setup lang="ts">
  import Textarea from 'primevue/textarea';
  import InputText from 'primevue/inputtext';
  import Donation from '@/types/Donation';

  const emit = defineEmits(['update']);
  const props = defineProps<{data: Donation}>();
  
</script>

<style scoped>
  .type-description {
    margin-bottom: 32px;
  }

  .amount-input {
    margin-bottom: 12px;
  }
</style>
