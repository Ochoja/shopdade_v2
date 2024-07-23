<script setup>
import { RouterLink, useRoute } from 'vue-router'
import Button from '@/components/TheButton.vue'
import { computed, onMounted, ref, watch } from 'vue'

const route = useRoute()
const current_path = computed(() => route.path)
const isLogin = ref(true)
const isSignUp = ref(false)

// Change Login and signup form depending on route
watch(current_path, () => {
  if (current_path.value.includes('/auth/sign-up')) {
    isSignUp.value = true
    isLogin.value = false
  } else if (current_path.value.includes('/auth/login')) {
    isLogin.value = true
    isSignUp.value = false
  }
})

onMounted(() => {
  if (current_path.value.includes('/auth/sign-up')) {
    isSignUp.value = true
    isLogin.value = false
  } else if (current_path.value.includes('/auth/login')) {
    isLogin.value = true
    isSignUp.value = false
  }
})
</script>

<template>
  <main class="grid grid-cols-auth min-h-[98vh]">
    <div class="md:rounded-3xl bg-white pt-6">
      <div class="text-center mb-14">
        <RouterLink to="/" class="font-logo text-primary text-2xl">shopDADE</RouterLink>
      </div>

      <form v-if="isLogin">
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

      <form v-if="isSignUp">
        <div class="form-title">
          <h2 class="font-semibold">Create an Account</h2>
          <p class="font-light">Welcome Back! Please enter your details.</p>
        </div>

        <div>
          <label for="name">Full Name*</label>
          <input type="text" id="name" placeholder="John Doe" required />
        </div>

        <div>
          <label for="email">Email*</label>
          <input type="email" id="email" placeholder="Enter your email" required />
        </div>

        <div>
          <label for="password">Password*</label>
          <input type="password" id="password" placeholder="Enter your password" required />
        </div>

        <div>
          <label for="retype_password">Retype Password*</label>
          <input type="password" id="retype_password" placeholder="Enter your password" required />
        </div>

        <Button size="large" class="w-[100%] mt-5">Create Account</Button>
        <p class="font-light mt-2 text-center text-[1.1rem]">
          Already have an account?
          <RouterLink to="/auth/login" class="font-bold text-primary">Sign In</RouterLink>
        </p>
      </form>
    </div>

    <div class="bg-auth bg-fixed bg-no-repeat bg-[100%] w-[103%] relative left-[-3%] z-[-5]"></div>
  </main>
</template>

<style lang="postcss" scoped>
form {
  @apply w-[60%] m-auto mb-24;
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
