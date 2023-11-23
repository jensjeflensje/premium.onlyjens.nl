<template>
  <div class="shadebar"></div>
</template>

<script setup lang="ts">
</script>

<style scoped>
  .shadebar {
    box-shadow: 0 -4px 5px rgba(53, 52, 52, 0.7);
    width: 100%;
    height: 10px;
    position: absolute;
    overflow-x: hidden;
    z-index: 1;
  }
</style>
