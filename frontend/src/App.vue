<script setup>
import { RouterView } from 'vue-router'
import TopNavigation from './components/TopNavigation.vue'
import TheFooter from './components/TheFooter.vue'
</script>

<template>
  <TopNavigation></TopNavigation>
  <RouterView></RouterView>
  <TheFooter></TheFooter>
</template>

<style lang="postcss">
h2 {
  @apply text-3xl font-bold;
}

.grid-width {
  @apply w-[95%] mx-auto;
}

.product-grid {
  @apply grid grid-cols-4 gap-4;
}
</style>
