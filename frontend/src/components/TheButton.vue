<script setup>
const props = defineProps({
  size: String,
  type: String
})

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
  <button :class="btnClass"></button>
  <button class="bg-primary text-white rounded-3xl py-2 px-6">
    <slot>Button</slot>
  </button>
</template>

<style lang="postcss">
.primary {
  @apply bg-primary text-white rounded-3xl;
}

.large {
  @apply text-lg;
}
</style>
