<template>
  <BaseDialog :dialog="{header: 'Payment failed', visible: dialogs.failedDialog}">
    Your payment didn't succeed.
    Please contact me on Discord (username: jensderouter) if this wasn't intended.
  </BaseDialog>
  <SuccessDialog :dialog="{visible: dialogs.successDialog}">
  </SuccessDialog>

  <BaseDialog :dialog="{header: '🚀 You\'re welcome!', visible: dialogs.helpDialog}">
    Hi, I figured I'd send your this site to let you know of the possibility to donate.
    I like helping people, and that's fine by itself,
    but I want to give people the opportunity to give back.
    It's completely voluntary, so please don't feel obligated to donate :)
  </BaseDialog>
  <BaseDialog :dialog="{header: '🚀 You\'re welcome!', visible: dialogs.openSourceDialog}">
    Hi, I figured I'd send your this site to let you know of the possibility to donate.
    It's totally fine to use my software free of charge,
    but I want to give people the opportunity to give back.
    It's completely voluntary, so please don't feel obligated to donate :)
  </BaseDialog>
</template>

<script setup lang="ts">
import BaseDialog from '@/components/dialogs/BaseDialog.vue';
import { checkPaymentIntent } from '@/api';
import { reactive } from 'vue';
import SuccessDialog from '@/components/dialogs/SuccessDialog.vue';

const urlParams = new URLSearchParams(window.location.search);
const dialogs = reactive({
  successDialog: false,
  failedDialog: false,
  helpDialog: false,
  openSourceDialog: false,
})

if (urlParams.get('payment_status')) {
  if (urlParams.get('payment_status') === 'completed' && urlParams.get('redirect_status') === 'succeeded') {
    try {
      localStorage.setItem('currentStripeId', urlParams.get('payment_intent')!);
      checkPaymentIntent();
      dialogs.successDialog = true;
    } catch {
      dialogs.failedDialog = true;
    }
  } else {
    dialogs.failedDialog = true;
  }
}

if (urlParams.get('from')) {
  switch (urlParams.get('from')) {
    case 'help':
      dialogs.helpDialog = true;
      break;
    case 'open_source':
      dialogs.openSourceDialog = true;
      break;
  }
}

</script>

<style scoped>
</style>
