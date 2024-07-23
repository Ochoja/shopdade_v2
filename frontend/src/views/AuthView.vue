<script setup>
import { RouterLink } from 'vue-router'
import Button from '@/components/TheButton.vue'
</script>

<template>
  <main class="grid grid-cols-auth min-h-[98vh]">
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
        <div class="text-right relative top-[-10px]">
          <RouterLink to="/" class="font-semibold text-primary text-sm"
            >Forgot Password?</RouterLink
          >
        </div>

        <Button size="large" class="w-[100%] mt-5">Login</Button>
        <p class="font-light mt-2 text-center text-[1.1rem]">
          Don't have an account?
          <RouterLink to="/auth/sign-up" class="font-bold text-primary">Sign Up</RouterLink>
        </p>
      </form>

      <form></form>
    </div>
    <div class="bg-auth bg-center w-[110%] relative left-[-10%] z-[-5]"></div>
  </main>
</template>

<style lang="postcss" scoped>
form {
  @apply w-[60%] m-auto;
}

.form-title {
  @apply text-center mb-7;
}

label {
  @apply block font-medium mb-1;
}

input {
  @apply block border-[#000] border-[1px] rounded-xl px-2 py-[0.9rem] mb-5 w-[100%] font-medium;
}
</style>
