<template>
  <div class="header">
    <div class="header-content">
      <img id="logo" src="../assets/jens.png" alt="">
      <h3 id="title">OnlyJens Premium</h3>
    </div>
  </div>
  <ShadeBar/>
</template>

<script setup lang="ts">
import ShadeBar from '@/components/ShadeBar.vue'
</script>

<style scoped>
  .header {
    background-image: url('../assets/banner.png');
    background-size: cover;
    background-position: center;
  }

  .header-content {
    backdrop-filter: blur(6px) saturate(0.6) contrast(1.2);
    -webkit-backdrop-filter: blur(6px) saturate(0.6) contrast(1.2);
    display: inline-block;
    text-align: center;
    width: 100%;
    padding: 48px 4px 96px 4px;
  }

  #logo {
    width: 120px;
    margin-bottom: -30px;
  }

  #title {
    font-size: 55px;
    display: inline-block;
    font-weight: 500;
    text-shadow: 2px 2px 2px var(--blue-400);
    margin: 0;
  }

  @media only screen and (max-width: 500px) {
    .header-content {
      backdrop-filter: blur(8px) saturate(0.4) contrast(1.2);
      -webkit-backdrop-filter: blur(8px) saturate(0.4) contrast(1.2);
      padding: 16px 4px;
    }
  }

  @media only screen and (max-width: 616px) {
    #logo {
      margin-bottom: 5px;
      width: 150px;
    }
  }
</style>
