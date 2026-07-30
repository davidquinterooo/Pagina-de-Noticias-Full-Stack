<script setup lang="ts">
import { ref } from 'vue'
definePageMeta({ layout: 'admin', middleware: 'admin' })

const { crearNoticia } = useNoticiasAdmin()
const router = useRouter()
const errorMsg = ref('')

const onSubmit = async (formData: FormData) => {
  errorMsg.value = ''
  try {
    await crearNoticia(formData)
    router.push('/admin')
  } catch {
    errorMsg.value = 'No se pudo guardar la noticia. Revisa los campos.'
  }
}
</script>

<template>
  <div>
    <h1 class="fs-3 fw-bold mb-4">Nueva noticia</h1>
    <div v-if="errorMsg" class="alert alert-danger">{{ errorMsg }}</div>
    <NoticiaForm @submit="onSubmit" />
  </div>
</template>