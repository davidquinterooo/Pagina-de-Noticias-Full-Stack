<script setup lang="ts">
import { ref } from 'vue'
definePageMeta({ layout: 'admin', middleware: 'admin' })

const route = useRoute()
const router = useRouter()
const { getNoticiaAdmin, actualizarNoticia } = useNoticiasAdmin()
const errorMsg = ref('')

const { data: noticia } = await useAsyncData(
  `admin-noticia-${route.params.slug}`,
  () => getNoticiaAdmin(route.params.slug as string)
)

const onSubmit = async (formData: FormData) => {
  errorMsg.value = ''
  try {
    await actualizarNoticia(route.params.slug as string, formData)
    router.push('/admin')
  } catch {
    errorMsg.value = 'No se pudo actualizar la noticia.'
  }
}
</script>

<template>
  <div>
    <h1 class="fs-3 fw-bold mb-4">Editar noticia</h1>
    <div v-if="errorMsg" class="alert alert-danger">{{ errorMsg }}</div>
    <NoticiaForm v-if="noticia" :noticia="noticia" @submit="onSubmit" />
  </div>
</template>