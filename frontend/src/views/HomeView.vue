<script setup>
import Button from '../components/TheButton.vue'
import Card from '../components/ProductCard.vue'
</script>

<template>
  <main class="grid-width">
    <section class="bg-hero bg-cover bg-right py-[8rem] px-8 rounded-[10px] mb-14">
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
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
      </div>

      <div class="text-center mt-8">
        <Button size="wide">See All</Button>
      </div>
    </section>
  </main>
</template>
