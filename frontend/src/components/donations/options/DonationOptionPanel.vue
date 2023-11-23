<template>
  <SelectButton
    v-model="donationType"
    :options="donationOptions"
    :allowEmpty="false"
    optionLabel="name"
    @change="handleTypeChange" />

  <div class="type-description">
    <component :is="donationType?.component" />
  </div>

  <InputNumber
    v-model="props.data.amount"
    class="amount-input"
    inputId="donationAmount"
    mode="currency"
    currency="EUR"
    locale="nl-NL"
    :disabled="donationType.value !== 'custom'"
    :min="donationType.amount" />

</template>

<script setup lang="ts">
  import SelectButton from 'primevue/selectbutton';
  import InputNumber from 'primevue/inputnumber';
  import { ref, shallowRef } from 'vue';
  import type DonationOption from '@/types/DonationOption'
  import DonationPanelCustomOption from '@/components/donations/options/DonationPanelCustomOption.vue';
  import DonationPanelSmallOption from '@/components/donations/options/DonationPanelSmallOption.vue';
  import Donation from '@/types/Donation';

  const emit = defineEmits(['update']);
  
  const props = defineProps<{data: Donation}>();

  const donationOptions = ref<DonationOption[]>([
    {
      name: 'Small',
      value: 'small',
      amount: 4,
      minAmount: 4,
      component: shallowRef(DonationPanelSmallOption),
    },
    {
      name: 'Custom',
      value: 'custom',
      amount: 10,
      minAmount: 5,
      component: shallowRef(DonationPanelCustomOption),
    },
  ]);

  const donationType = ref<DonationOption>(donationOptions.value[0]);

  function handleTypeChange() : void {
    props.data.amount = donationType.value.amount;
  }
  handleTypeChange();
</script>

<style scoped>
  .type-description {
    margin-bottom: 32px;
  }

  .amount-input {
    margin-bottom: 12px;
  }
</style>
