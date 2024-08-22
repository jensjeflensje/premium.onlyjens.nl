<template>
  <div id="main">
    <Header/>
    <RouterView />
    <Dialogs/>
  </div>
</template>

<script setup lang="ts">
import Dialogs from '@/components/dialogs/Dialogs.vue'
import Header from '@/components/Header.vue'
</script>

<style scoped>
</style>
