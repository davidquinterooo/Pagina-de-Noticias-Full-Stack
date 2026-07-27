<script setup lang="ts">
import { ref, watch } from 'vue';
const { getNoticias } = useNoticias();
const page = ref(1);

// const { data, status, error, refresh } = await useAsyncData(
//   () => `noticias-page-${page.value}`,
//   () => getNoticias({ page: page.value }),
//   { default: () => ({ count: 0, next: null, previous: null, results: [] }) }
// )

const route = useRoute()
const busqueda = ref((route.query.q as string) || '')

const { data, status, error, refresh } = await useAsyncData(
  () => `noticias-page-${page.value}-search-${busqueda.value}`,
  () => getNoticias({ page: page.value, search: busqueda.value || undefined })
)
// Si el usuario busca de nuevo desde el overlay estando ya en el home,
// reacciona al cambio del query param
watch(() => route.query.q, (nuevoQ) => {
  busqueda.value = (nuevoQ as string) || ''
  page.value = 1
  refresh()
})
const cambiarPagina = (nuevaPagina: number) => {
  page.value = nuevaPagina;
  refresh();
};
</script>

<template>
  <div class="container py-4">
    <div v-if="status === 'pending'" class="text-center py-5">
      Cargando noticias...
    </div>

    <div v-else-if="error" class="alert alert-danger">
      No se pudieron cargar las noticias.
    </div>

    <ul v-else class="list-unstyled p-0 row gx-2 gy-5 justify-content-evenly">
      <NoticiaCard
        v-for="noticia in data?.results ?? []"
        :key="noticia.id"
        :noticia="noticia"
      />
    </ul>

    <!-- Paginación simple -->
    <nav v-if="data && (data.next || data.previous)" class="mt-4">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: !data.previous }">
          <button class="page-link" @click="cambiarPagina(page - 1)">
            Anterior
          </button>
        </li>
        <li class="page-item" :class="{ disabled: !data.next }">
          <button class="page-link" @click="cambiarPagina(page + 1)">
            Siguiente
          </button>
        </li>
      </ul>
    </nav>
  </div>
</template>
