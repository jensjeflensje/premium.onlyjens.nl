<template>
  <div id="checkout"></div>
</template>

<script setup lang="ts">
  import Donation from '@/types/Donation';
  import { BASE_URL, createPaymentIntent, stripe } from '@/api';
  import { ref } from 'vue';
  import { StripeElements, StripePaymentElement } from '@stripe/stripe-js';

  const emit = defineEmits(['update']);
  const props = defineProps<{data: Donation}>();
  defineExpose({complete,})

  const processing = ref(true);
  let paymentElement: StripePaymentElement;
  let elements: StripeElements;

  createPaymentIntent(props.data).then(async clientSecret => {
    const appearance = {
      theme: 'night',
      variables: {
        colorPrimary: '#60a5fa',
        colorBackground: '#22272E',
        fontFamily: 'Inter var, system-ui, sans-serif',
      }
    };
    const options = {
      layout: {
        type: 'tabs',
        defaultCollapsed: false,
      }
    };
    // @ts-ignore
    elements = stripe!.elements({ clientSecret, appearance });
    // @ts-ignore
    paymentElement = elements.create('payment', options);
    paymentElement.mount('#checkout');
    processing.value = false;
  });

  async function complete() {
    processing.value = true;
    try {
      stripe!.confirmPayment({
        elements,
        confirmParams: {
          return_url: `${BASE_URL}?payment_status=completed`
        }
      });
    } finally {
      processing.value = false;
    }
  }

</script>

<style scoped>
  .complete-button {
    margin-top: 12px;
  }
</style>
