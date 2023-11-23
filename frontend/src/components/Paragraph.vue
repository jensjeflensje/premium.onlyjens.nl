<template>
  <div class="paragraph">
    <component :is="header" class="paragraph-emoji">{{ emoji }}</component>
    <div class="paragraph-content">
      <div class="paragraph-title">
        <component :is="header">{{ title }}</component>
      </div>
      
      <slot name="content"></slot>
    </div>
  </div>
  
</template>

<script setup lang="ts">
defineProps<{ header: string, emoji: string, title: string }>()
</script>

<style scoped>
  h2, h3, h4, h5, h6 {
    font-weight: 500;
  }

  .paragraph-title {
    text-underline-offset: 8px;
  }

  .paragraph-title > h1 {
    text-decoration: underline var(--blue-100) 2px;
  }

  .paragraph-title > h2, h3, h4, h5, h6 {
    text-decoration: underline var(--blue-100) 1px;
  }

  .paragraph {
    display: flex;
    gap: 16px;
    margin-bottom: 18px;
  }
</style>
