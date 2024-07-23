<script setup>
import { useRoute } from 'vue-router'
import { RouterView } from 'vue-router'
import TopNavigation from './components/TopNavigation.vue'
import TheFooter from './components/TheFooter.vue'
import { computed, ref, watch } from 'vue'

const route = useRoute()
const path = computed(() => route.path)

// show Navigation bar depending on path
const showNav = ref(true)
watch(path, () => {
  if (path.value.includes('auth')) {
    showNav.value = false
  } else {
    showNav.value = true
  }
})
</script>

<template>
  <TopNavigation v-show="showNav"></TopNavigation>
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
  @apply grid grid-cols-3 gap-x-4 gap-y-6  md:grid-cols-4 md:gap-x-6 md:gap-y-8 lg:grid-cols-5;
}
</style>
