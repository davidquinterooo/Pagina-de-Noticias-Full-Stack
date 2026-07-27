<script setup lang="ts">
const route = useRoute();
const { getNoticiaPorSlug } = useNoticias();

const {
  data: noticia,
  status,
  error,
} = await useAsyncData(`noticia-${route.params.slug}`, () =>
  getNoticiaPorSlug(route.params.slug as string),
);

useSeoMeta({
  title: () => noticia.value?.titulo,
  description: () => noticia.value?.resumen,
  ogImage: () =>
    noticia.value ? useMediaUrl(noticia.value.imagen_portada) : "",
});
</script>

<template>
  <div class="container py-4">
    <div v-if="status === 'pending'">Cargando...</div>
    <div v-else-if="error" class="alert alert-danger">
      Noticia no encontrada.
    </div>

    <article class="container" v-else-if="noticia">
      <h1 class="fw-bold text-black fs-1">{{ noticia.titulo }}</h1>
      <p class="fs-6 text-dark">
        Publicado:
        {{ new Date(noticia.fecha_publicacion).toLocaleDateString() }}
      </p>
      <p class="fw-bold text-black fs-5">{{ noticia.resumen }}</p>
      <img
        :src="useMediaUrl(noticia.imagen_portada)"
        :alt="noticia.imagen_portada_alt"
        class="img-fluid rounded mb-4"
      />
      <p class="fs-6 text-dark">{{ noticia.imagen_portada_alt }}</p>
      <div
        class="text-black fs-5 container mx-1"
        v-html="noticia.contenido"
      ></div>
    </article>

    <div v-else class="alert alert-warning">Noticia no encontrada.</div>
  </div>
</template>
