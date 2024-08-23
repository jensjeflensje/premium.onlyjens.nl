<template>
  <div id="donation-box" v-if="currentDonation">
    <img src="../assets/jens.png">
    <div>
      <span class="bold-text">{{currentDonation.author}}</span>
      heeft
      <span class="bold-text">€{{currentDonation.amount}}</span>
      gedoneerd.
    </div>
    <div v-if="currentDonation.message">{{ currentDonation.message }}</div>
  </div>
  <audio ref="donationAudio" preload="auto">
    <source src="../assets/donation-sound.mp3"/>
  </audio>
</template>

<script setup lang="ts">

import { nextTick, onMounted, Ref, ref } from 'vue';
import Donation from '@/types/Donation.ts';
import { WS_URL } from '@/api.ts';

const donationAudio: Ref<HTMLAudioElement | undefined> = ref();
const currentDonation: Ref<Donation | undefined> = ref();
const donations: Ref<Donation[]> = ref([]);

function nextDonation() {
  currentDonation.value = undefined;
  nextTick(() => {
    if (donations.value.length) {
      currentDonation.value = donations.value.shift();
      donationAudio.value!.play();
      setTimeout(nextDonation, 5000);
    }
  });
}

function showOrQueueDonation(donation: Donation) {
  donations.value.push(donation);
  if (!currentDonation.value) {
    // immediately show
    nextDonation();
  }
}

let ws;

function connectWs() {
  console.log(`Conecting to WebSocket URL: ${WS_URL}`);
  ws = new WebSocket(`${WS_URL}/ws/donations/`);

  ws.onopen = function(){
    console.log("WebSocket connected!");
  }

  ws.onmessage = function(msg) {
      console.log(JSON.parse(msg.data).message);
      showOrQueueDonation(JSON.parse(msg.data));
  }

  ws.onclose = () => setTimeout(connectWs, 1000);
}

onMounted(connectWs);

</script>

<style scoped>
  @keyframes fade-in {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  #donation-box {
    animation: fade-in 700ms;
    display: flex;
    flex-direction: column;
    justify-content: center;
    row-gap: 16px;
  }

  #donation-box > * {
    width: 250px;
    text-align: center;
  }

  .bold-text {
    color: var(--blue-300);
    font-weight: bold;
  }

</style>