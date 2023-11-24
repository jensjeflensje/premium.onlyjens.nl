<template>
  <BaseDialog :dialog="{header: 'Payment succeeded', visible: props.dialog.visible}">
    Thanks for your donation!
    As a show of gratitude, I would like to reward you with a certificate.
    <br/>
    <img v-if="imageSrc" :src="imageSrc" />
    <ProgressSpinner v-else="imageSrc" />
  </BaseDialog>
</template>

<script setup lang="ts">
import { getCertificate } from '@/api';
import BaseDialog from '@/components/dialogs/BaseDialog.vue';
import ProgressSpinner from 'primevue/progressspinner';
import { ref } from 'vue';
const props = defineProps<{
  dialog: {
    visible: boolean,
  }
}>();

const imageSrc = ref("")

if (props.dialog.visible) {
  const imageTask = setInterval(async () => {
    const result = await getCertificate();
    if (result !== null) {
      imageSrc.value = result;
      clearInterval(imageTask);
    }
  }, 1000);
}

</script>

<style scoped>
img {
  width: 100%;
}
</style>
