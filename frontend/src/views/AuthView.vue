<script setup>
import { RouterLink, useRoute } from 'vue-router'
import Button from '@/components/TheButton.vue'
import { computed, onMounted, ref, watch, watchEffect } from 'vue'
import axios from 'axios'

const route = useRoute()
const current_path = computed(() => route.path)
const isLogin = ref(true)
const isSignUp = ref(false)
const isLoading = ref(false)

/* Sign Up Logic */
const password = ref('')
const confirm_password = ref('')
const full_name = ref('')
const email = ref('')
const matching_pw = ref(true)

watchEffect(() => {
  if (password.value !== confirm_password.value) {
    matching_pw.value = false
  } else {
    matching_pw.value = true
  }
})

async function signUp() {
  if (matching_pw.value) {
    try {
      isLoading.value = true
      const response = await axios.post('http://127.0.0.1:5000/api/sign_up/', {
        full_name: full_name.value,
        email: email.value,
        password: password.value
      })
      isLoading.value = false
      console.log(response.data)
    } catch (error) {
      console.log(error)
    }
  }
}
/* End Sign Up Logic */

/* Route and Form Logic */
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

// Put right form (login or signup) when component is mounted
onMounted(() => {
  if (current_path.value.includes('/auth/sign-up')) {
    isSignUp.value = true
    isLogin.value = false
  } else if (current_path.value.includes('/auth/login')) {
    isLogin.value = true
    isSignUp.value = false
  }
})
/* End Route and Form Logic */
</script>

<template>
  <main class="grid md:grid-cols-auth min-h-[80vh]">
    <div class="md:rounded-3xl bg-white">
      <div class="text-center mb-14 pt-6">
        <RouterLink to="/" class="font-logo text-primary text-2xl">shopDADE</RouterLink>
      </div>

      <form v-if="isLogin" @submit.prevent="login">
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

      <form v-if="isSignUp" @submit.prevent="signUp">
        <div class="form-title">
          <h2 class="font-semibold">Create an Account</h2>
          <p class="font-light">Welcome Back! Please enter your details.</p>
        </div>

        <div>
          <label for="name">Full Name*</label>
          <input v-model="full_name" type="text" id="name" placeholder="John Doe" required />
        </div>

        <div>
          <label for="email">Email*</label>
          <input v-model="email" type="email" id="email" placeholder="Enter your email" required />
        </div>

        <div>
          <label for="password">Password*</label>
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="Enter your password"
            required
          />
        </div>

        <div>
          <label for="retype_password">Retype Password*</label>
          <input
            v-model="confirm_password"
            type="password"
            id="retype_password"
            placeholder="Enter your password"
            required
          />
        </div>
        <div v-show="!matching_pw" class="relative top-[-14px] font-semibold text-sm text-primary">
          Passwords do not match
        </div>

        <Button size="large" class="w-[100%] mt-5">
          <span v-if="isLoading">Loading....</span>
          <span v-else>Create Account</span>
        </Button>
        <p class="font-light mt-2 text-center text-[1.1rem]">
          Already have an account?
          <RouterLink to="/auth/login" class="font-bold text-primary">Sign In</RouterLink>
        </p>
      </form>
    </div>

    <div
      class="hidden md:block bg-auth bg-fixed bg-no-repeat bg-[100%] w-[103%] relative left-[-3%] z-[-5]"
    ></div>
  </main>
</template>

<style lang="postcss" scoped>
form {
  @apply w-[75%] lg:w-[60%] m-auto mb-24;
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
