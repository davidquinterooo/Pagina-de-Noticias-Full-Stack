
<script setup lang="ts">
interface Noticia {
  id: number
  titulo: string
  slug: string
  resumen: string
  imagen_portada: string
  imagen_portada_alt: string
  fecha_publicacion: string
}

const props = defineProps<{
  noticia: Noticia
}>()

const imagenUrl = computed(() => useMediaUrl(props.noticia.imagen_portada))
</script>

<template>
  <li class="col-12 col-sm-6 col-md-auto">
    <div class="card-hover w-100" style="max-width: 17rem;">
      <NuxtLink
        class="links-card"
        :to="`/noticias/${noticia.slug}`"
        style="text-decoration: none;"
      >
        <img
          :src="imagenUrl"
          :alt="noticia.imagen_portada_alt || noticia.titulo"
          class="card-img-top w-100"
          style="height: 160px; object-fit: cover; border-radius: 5px;"
        >
        <p class="fs-5 lh-1 fw-bold mt-2">
          {{ noticia.titulo }}
        </p>
      </NuxtLink>
    </div>
  </li>
</template>