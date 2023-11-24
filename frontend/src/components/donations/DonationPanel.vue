<template>
  <h1>Donation</h1>
  <p v-if="currentStep === 0">
    If you want, you can support my efforts by sending a (small) donation.
  </p>

  <div>
    <component ref="currentStepComponent" :is="steps[currentStep]" :data="donationData"/>
  </div>

  <Button
    v-if="currentStep !== 0"
    link
    class="step-button back-button"
    label="Back"
    size="small"
    icon="pi pi-angle-left"
    @click="currentStep--" />

  <Button
    class="step-button"
    :label="currentStep + 1 !== steps.length ? 'Proceed' : 'Complete'"
    size="small"
    icon="pi pi-angle-right"
    iconPos="right"
    @click="nextStep" />
</template>

<script setup lang="ts">
  import DonationCheckoutPanel from '@/components/donations/DonationCheckoutPanel.vue';
  import DonationMessagePanel from '@/components/donations/DonationMessagePanel.vue';
  import DonationOptionPanel from '@/components/donations/options/DonationOptionPanel.vue';
  import Donation from '@/types/Donation';
  import Button from 'primevue/button';
  import { reactive, ref } from 'vue';

  const currentStepComponent = ref<{complete: Function}>();

  const steps = [
    DonationOptionPanel,
    DonationMessagePanel,
    DonationCheckoutPanel,
  ];

  const currentStep = ref(0);
  const donationData = reactive<Donation>({
    amount: 0,
    author: '',
    message: '',
  });

  function nextStep() {
    if (currentStep.value + 1 === steps.length) {
      currentStepComponent.value!.complete();
      return;
    }
    currentStep.value++
  }
</script>

<style scoped>
  .step-button {
    margin-top: 12px;
  }
  .back-button {
    margin-right: 12px;
  }
</style>
