<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  product: Object
})
</script>

<template>
  <RouterLink
    :to="`/product/${product._id}`"
    class="rounded-lg text-sm cursor-pointer m-auto w-[100%]"
  >
    <div class="relative w-[100%] pt-[100%]">
      <img
        :src="product.images[0]"
        class="w-[100%] h-[100%] absolute top-0 left-0 rounded-md object-cover"
      />
    </div>

    <div class="mb-1 mt-2 font-semibold">{{ product.name }}</div>
    <div class="font-medium">${{ product.price }}</div>
  </RouterLink>
</template>
