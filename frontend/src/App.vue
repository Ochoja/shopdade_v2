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
.grid-width {
  @apply w-[95%] mx-auto;
}
</style>
