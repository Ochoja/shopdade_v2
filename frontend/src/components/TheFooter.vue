<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <footer class="pt-8 pb-1 bg-primary text-white">
    <div class="grid-width flex justify-between flex-wrap gap-8 mb-16">
      <div>
        <div class="text-2xl font-logo">shopDADE</div>
        <div class="text-sm max-w-[24.5rem]">
          Discover our latest arrivals, curated for the modern working class, shop now to elevate
          your wardrobe with fresh sophistication and style.
        </div>
      </div>
      <div class="group">
        <h3>Collection</h3>
        <RouterLink to="/">Suit</RouterLink>
        <RouterLink to="/">Footwear</RouterLink>
        <RouterLink to="/">Accesories</RouterLink>
        <RouterLink to="/">Tops</RouterLink>
        <RouterLink to="/">Bottoms</RouterLink>
      </div>
      <div class="group">
        <h3>Company</h3>
        <div>Privacy Policy</div>
        <div>Terms of Service</div>
        <div>Customer Care</div>
      </div>
      <div class="group">
        <h3>Social Media</h3>
      </div>
    </div>

    <div class="text-center">
      <RouterLink to="/" class="text-xs hover:underline">Copyright ShopDade 2024</RouterLink>
    </div>
  </footer>
</template>

<style lang="postcss" scoped>
.group {
  @apply flex flex-col gap-1;
}

.group h3 {
  @apply text-lg font-bold;
}

.group div {
  @apply font-light;
}

.group a {
  @apply no-underline;
}
</style>
