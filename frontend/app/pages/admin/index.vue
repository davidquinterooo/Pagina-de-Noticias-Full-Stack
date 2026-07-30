<script setup lang="ts">
import { ref } from 'vue'
definePageMeta({ layout: 'admin', middleware: 'admin' })

const { getNoticiasAdmin, eliminarNoticia } = useNoticiasAdmin()
const page = ref(1)

const { data, refresh } = await useAsyncData(
  () => `admin-noticias-page-${page.value}`,
  () => getNoticiasAdmin({ page: page.value })
)

const onEliminar = async (slug: string) => {
  if (!confirm('¿Eliminar esta noticia? Esta acción no se puede deshacer.')) return
  await eliminarNoticia(slug)
  refresh()
}
</script>

<template>
  <div>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="fs-3 fw-bold">Noticias</h1>
      <NuxtLink to="/admin/noticias/nueva" class="btn btn-dark">+ Nueva noticia</NuxtLink>
    </div>

    <table class="table">
      <thead>
        <tr><th>Título</th><th>Estado</th><th>Publicación</th><th></th></tr>
      </thead>
      <tbody>
        <tr v-for="noticia in data?.results ?? []" :key="noticia.id">
          <td>{{ noticia.titulo }}</td>
          <td>
            <span :class="noticia.estado === 'publicado' ? 'badge bg-success' : 'badge bg-secondary'">
              {{ noticia.estado }}
            </span>
          </td>
          <td>{{ noticia.fecha_publicacion ? new Date(noticia.fecha_publicacion).toLocaleDateString() : '—' }}</td>
          <td class="text-end">
            <NuxtLink :to="`/admin/noticias/${noticia.slug}`" class="btn btn-sm btn-outline-secondary me-2">Editar</NuxtLink>
            <button class="btn btn-sm btn-outline-danger" @click="onEliminar(noticia.slug)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>