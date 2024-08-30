<script setup>
import { Icon } from '@iconify/vue/dist/iconify.js'
import { useRouter } from 'vue-router'

const props = defineProps({
  size: String,
  type: String,
  icon: String,
  to: String
})

const router = useRouter()

// Go to route based on route props
function goToRoute() {
  if (props.to) {
    router.push(props.to)
  }
  return
}

// Apply right class to button based on props
const btnClass = () => {
  if (props.type && props.size) {
    return `${props.type} ${props.size}`
  } else if (props.size && !props.type) {
    return `primary ${props.size}`
  } else if (props.type && !props.size) {
    return `${props.type}`
  } else {
    return 'primary'
  }
}
</script>

<template>
  <button :class="btnClass()" @click="goToRoute()">
    <Icon v-if="props.icon" :icon="props.icon"></Icon>
    <slot></slot>
  </button>
</template>

<style lang="postcss">
button {
  @apply rounded-full px-4 py-2 flex justify-center;
}

.primary {
  @apply bg-primary text-white;
}

.secondary {
  @apply text-primary bg-white border-primary border-2;
}

.large {
  @apply text-2xl py-4 px-8;
}

.wide {
  @apply font-semibold px-12;
}
</style>
