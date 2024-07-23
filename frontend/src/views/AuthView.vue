<script setup>
import { RouterLink } from 'vue-router'
import Button from '@/components/TheButton.vue'
</script>

<template>
  <main class="grid grid-cols-auth min-h-[85vh]">
    <div class="md:rounded-3xl bg-white pt-6">
      <div class="text-center mb-14">
        <RouterLink to="/" class="font-logo text-primary text-2xl">shopDADE</RouterLink>
      </div>

      <form>
        <div class="form-title">
          <h2 class="font-semibold">Sign In</h2>
          <p class="font-light">Welcome Back! Please enter your details.</p>
        </div>

        <div>
          <label for="email">Email</label>
          <input type="email" id="email" placeholder="Enter your email" required />
        </div>

        <div>
          <label for="password">Password</label>
          <input type="password" id="password" placeholder="Enter your password" required />
        </div>

        <Button size="large">Login</Button>
      </form>

      <form></form>
    </div>
    <div class="bg-auth bg-center w-[110%] relative left-[-10%] z-[-5]"></div>
  </main>
</template>

<style lang="postcss" scoped>
form {
  @apply w-[80%] m-auto;
}

.form-title {
  @apply text-center;
}
</style>
