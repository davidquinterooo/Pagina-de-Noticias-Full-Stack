<script setup lang="ts">
import { ref } from 'vue'
definePageMeta({ layout: false })

const { login } = useAuth()
const username = ref('')
const password = ref('')
const errorMsg = ref('')
const cargando = ref(false)

const onSubmit = async () => {
  errorMsg.value = ''
  cargando.value = true
  try {
    await login(username.value, password.value)
    await navigateTo('/admin')
  } catch {
    errorMsg.value = 'Usuario o contraseña incorrectos.'
  } finally {
    cargando.value = false
  }
}
</script>

<template>
  <div class="d-flex align-items-center justify-content-center vh-100 bg-light">
    <form @submit.prevent="onSubmit" class="p-4 bg-white rounded shadow" style="width: 320px;">
      <h1 class="fs-4 fw-bold mb-3">Iniciar sesión</h1>
      <div class="mb-3">
        <label class="form-label">Usuario</label>
        <input v-model="username" type="text" class="form-control" required />
      </div>
      <div class="mb-3">
        <label class="form-label">Contraseña</label>
        <input v-model="password" type="password" class="form-control" required />
      </div>
      <div v-if="errorMsg" class="alert alert-danger py-2">{{ errorMsg }}</div>
      <button type="submit" class="btn btn-dark w-100" :disabled="cargando">
        {{ cargando ? 'Ingresando...' : 'Ingresar' }}
      </button>
    </form>
  </div>
</template>