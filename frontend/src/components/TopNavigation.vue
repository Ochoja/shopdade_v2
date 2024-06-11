<script setup>
import { ref } from 'vue'
import { Icon } from '@iconify/vue'

const showCategory = ref(false)
const selectedCategory = ref('All Category')
const category = ref([
  'All Category',
  'Suit',
  'Footwear',
  'Accesories',
  'Tops',
  'Bottoms',
  'Jacket'
])
const categoryRef = ref([])

function changeCategory(index) {
  selectedCategory.value = categoryRef.value[index].innerHTML
  showCategory.value = !showCategory.value
}
</script>

<template>
  <nav class="flex grid-width items-center justify-between py-2">
    <div class="font-logo text-primary text-2xl">shopDADE</div>
    <div
      class="flex border-[1px] border-[#F34213] p-[0.4rem] rounded-full items-center font-bold text-sm relative"
    >
      <div
        @click="showCategory = !showCategory"
        class="pl-3 pr-3 flex items-center gap-1 cursor-pointer min-w-26"
      >
        {{ selectedCategory }} <Icon icon="raphael:arrowdown"></Icon>
      </div>
      <div
        v-show="showCategory"
        class="absolute top-12 bg-white rounded-md border-primary border-[1.5px]"
      >
        <div
          @click="changeCategory(index)"
          ref="categoryRef"
          v-for="(item, index) in category"
          :key="index"
          class="hover:bg-primary px-4 py-1 text-center rounded-md cursor-pointer hover:text-white"
        >
          {{ item }}
        </div>
      </div>
      <input
        type="search"
        placeholder="Browse your favorite products"
        maxlength="50"
        class="border-0 focus:outline-none w-96 border-l-2 p-2 border-[rgba(0,0,0,0.4)]"
      />
      <div class="px-6 py-2 bg-primary rounded-3xl cursor-pointer">
        <Icon icon="lucide:search" class="text-[#fff] text-[1.5rem]"></Icon>
      </div>
    </div>

    <div class="font-bold flex text-lg gap-6">
      <div class="flex items-center gap-1 cursor-pointer">
        Cart <Icon icon="mdi:cart" class="text-2xl"></Icon>
      </div>
      <div class="cursor-pointer flex gap-1 items-center">
        <div>Daniel Ochoja</div>
        <div class="rounded-full bg-primary h-10 w-10"></div>
      </div>
    </div>
  </nav>
</template>
