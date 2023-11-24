<template>
  <Dialog
    v-model:visible="visible"
    modal
    dismissableMask
    :draggable="false"
    :header="props.dialog.header"
    :style="{ maxWidth: '50rem', margin: '18px' }"
  >
    <p>
      <slot/>
    </p>
  </Dialog>
</template>

<script setup lang="ts">
import Dialog from 'primevue/dialog';
import { ref } from 'vue';
const props = defineProps<{
  dialog: {
    visible: boolean,
    header: string,
  }
}>();
const visible = ref(props.dialog.visible);
</script>

<style scoped>
</style>
