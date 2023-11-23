import type { Component } from 'vue';

export default interface DonationOption {
  name: string;
  value: string;
  component: Component;
  amount: number;
  minAmount: number;
}