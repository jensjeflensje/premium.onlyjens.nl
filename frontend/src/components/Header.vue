<template>
  <div class="header">
    <div class="header-content">
      <img id="logo" src="../assets/jens.png" alt="">
      <h3 id="title">OnlyJens Premium</h3>
      <div class="social-container">
        <a v-for="account in socialAccounts" :href="account.link" target="_blank">
          <font-awesome-icon :icon="'fa-brands ' + account.icon"></font-awesome-icon>
        </a>
      </div>
    </div>
  </div>
  <ShadeBar/>
</template>

<script setup lang="ts">
import ShadeBar from '@/components/ShadeBar.vue'

const socialAccounts = [
  {icon: 'fa-github', link: 'https://github.com/jensjeflensje'},
  {icon: 'fa-youtube', link: 'https://www.youtube.com/@jederu'},
  {icon: 'fa-discord', link: 'https://discord.gg/U8DN52byBG'},
  {icon: 'fa-linkedin', link: 'https://www.linkedin.com/in/jens-de-ruiter-7557551b1/'},
]
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
    padding: 48px 4px 32px 4px;
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

  .social-container {
    margin-top: 36px;
    display: flex;
    gap: 12px;
    justify-content: center;
  }

  svg { 
    color: #f1f1ff;
    font-size: 24px;
    transition: all 300ms;
  }

  svg:hover {
    transform: scale(1.1);
    color: var(--blue-300);
  }

  @media only screen and (max-width: 500px) {
    .header-content {
      backdrop-filter: blur(8px) saturate(0.4) contrast(1.2);
      -webkit-backdrop-filter: blur(8px) saturate(0.4) contrast(1.2);
      padding: 16px 4px;
    }
    
    .social-container {
      margin-top: 16px;
      margin-bottom: 6px;
    }
  }

  @media only screen and (max-width: 616px) {
    #logo {
      margin-bottom: 5px;
      width: 150px;
    }
  }
</style>
