<script setup>
import Button from '../components/TheButton.vue'
import Card from '../components/ProductCard.vue'
import { RouterLink } from 'vue-router'

const products = [
  {
    _id: "ObjectId('669684a9b3c0c84813a5bb92')",
    name: 'Navy Blue Slim Fit Suit',
    description:
      "Elevate your elegance with this navy blue suit. Tailored to perfection, it's ideal for weddings, business meetings, or any special event.",
    price: 299.99,
    category: 'Suit',
    sizes: ['36R', '38R', '40R', '42R'],
    uom: 'US',
    images: ['https://dorsetsuits.co.nz/wp-content/uploads/2022/08/FT5-Product-Image2.jpg'],
    quantity: 15
  },
  {
    _id: "ObjectId('669684a9b3c0c84813a5bb92')",
    name: 'Navy Blue Slim Fit Suit',
    description:
      "Elevate your elegance with this navy blue suit. Tailored to perfection, it's ideal for weddings, business meetings, or any special event.",
    price: 299.99,
    category: 'Suit',
    sizes: ['36R', '38R', '40R', '42R'],
    uom: 'US',
    images: ['https://dorsetsuits.co.nz/wp-content/uploads/2022/08/FT5-Product-Image2.jpg'],
    quantity: 15
  }
]
</script>

<template>
  <main class="grid-width">
    <section class="bg-hero bg-cover bg-right py-[8rem] px-8 rounded-[10px] mb-16">
      <div class="max-w-[50%]">
        <p class="text-xl mb-3 text-white">
          Elevate your everyday style effortlessly with
          <span class="text-primary font-bold">shopDADE</span>. Discover a curated selection of
          sophisticated yet versatile gentlemen and lady's official and casual wears tailored for
          the modern working class.
        </p>

        <Button>Start Shopping</Button>
      </div>
    </section>

    <section>
      <div class="text-center mb-4">
        <h2>New Arrivals</h2>
        <p class="max-w-[95%] sm:max-w-[90%] md:max-w-[60%] mx-auto">
          Introducing our latest arrivals, meticulously curated to elevate your wardrobe with fresh
          sophistication and style
        </p>
      </div>

      <div class="product-grid">
        <Card v-for="(product, index) in products" :key="index" :product="product"></Card>
      </div>

      <div class="text-center mt-8">
        <Button size="wide">See All</Button>
      </div>
    </section>

    <section class="mt-[5rem] mb-[6rem]">
      <h2 class="text-center mb-6">Our Collections</h2>

      <div class="grid grid-cols-category gap-2 h-[85vh]">
        <RouterLink to="/" class="row-span-3 bg-footwear category">Footwear</RouterLink>
        <RouterLink to="/" class="row-span-5 bg-suit category">Suit</RouterLink>
        <RouterLink to="/" class="row-span-3 bg-accesory category">Accesories</RouterLink>
        <RouterLink to="/" class="row-span-5 bg-top category">Tops</RouterLink>
        <RouterLink to="/" class="row-span-5 bg-bottom category">Bottom</RouterLink>
        <RouterLink to="/" class="row-span-3 bg-jacket category">Jacket</RouterLink>
      </div>
    </section>
  </main>
</template>

<style lang="postcss" scoped>
.category {
  @apply bg-center bg-cover flex justify-center items-center text-white rounded-md font-semibold text-2xl;
}
</style>
