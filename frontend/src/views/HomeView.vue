<template>
  <div class="container-wrapper">
    <div class="container">
      <div class="child-container aboutme-container">
        <AboutMe/>
      </div>
      <div class="child-container donation-container">
        <DonationPanel/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AboutMe from '@/components/AboutMe.vue'
import DonationPanel from '@/components/donations/DonationPanel.vue';
</script>

<style scoped>
  .container-wrapper {
    margin: 24px;
  }

  .container {
    max-width: 1300px;
    margin: 10px auto;
    display: flex;
    gap: 24px 100px;
  }


  .aboutme-container {
    max-width: 925px;
  }

  .donation-container {
    max-width: 325px;
    min-width: 300px;
  }

  @media only screen and (max-width: 900px) {
    .container {
      flex-wrap: wrap;
    }

    .child-container {
      flex: 1 0 50%;
      max-width: 100%;
    }
  }
</style>
