<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

const { isOpen, close } = useSearchOverlay()
const { getNoticias } = useNoticias()

const termino = ref('')
const inputRef = ref<HTMLInputElement | null>(null)

const resultados = ref<any[]>([])
const buscando = ref(false)
const busquedaRealizada = ref(false)

let debounceTimer: ReturnType<typeof setTimeout>

const buscarEnVivo = (texto: string) => {
  clearTimeout(debounceTimer)

  if (!texto.trim()) {
    resultados.value = []
    busquedaRealizada.value = false
    return
  }

  debounceTimer = setTimeout(async () => {
    buscando.value = true
    try {
      const respuesta = await getNoticias({ search: texto })
      resultados.value = respuesta.results
    } finally {
      buscando.value = false
      busquedaRealizada.value = true
    }
  }, 400)
}

watch(termino, (nuevoTexto) => {
  buscarEnVivo(nuevoTexto)
})

const irADetalle = (slug: string) => {
  close()
  navigateTo(`/noticias/${slug}`)
}

const buscar = () => {
  const query = termino.value.trim()
  close()
  navigateTo(query ? `/?q=${encodeURIComponent(query)}` : '/')
}

// Enfoca el input automáticamente al abrir, y limpia el estado anterior
watch(isOpen, async (abierto) => {
  if (abierto) {
    termino.value = ''
    resultados.value = []
    busquedaRealizada.value = false
    await nextTick()
    inputRef.value?.focus()
  }
})

const onKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Escape') close()
}
</script>

<template>
  <Teleport to="body">
    <div
      v-if="isOpen"
      class="search-overlay"
      @keydown="onKeydown"
    >
      <div class="container-fluid h-100 d-flex flex-column">
        <div class="row align-items-center py-3">
          <div class="col-3">
            <NuxtLink
              class="navbar-brand fs-2 nav-link fw-bold"
              to="/"
              style="text-decoration: none;"
            >
              Name Page
            </NuxtLink>
          </div>

          <div class="col-6">
            <form @submit.prevent="buscar">
              <input
                ref="inputRef"
                v-model="termino"
                type="search"
                class="input-buscador shadow-none form-control form-control-lg"
                placeholder="Buscar noticias..."
              />
            </form>
          </div>

          <div class="col-3 text-end">
            <button type="button" class="btn btn-link fs-6 text-dark" @click="close">
              <BootstrapIcon name="x-lg" />
            </button>
          </div>
        </div>

        <!-- Resultados en vivo -->
        <div class="row justify-content-center flex-grow-1 overflow-auto">
          <div class="col-6">
            <div v-if="buscando" class="text-center text-muted py-4">
              Buscando...
            </div>

            <div v-else-if="busquedaRealizada && resultados.length === 0" class="text-center text-muted py-4">
              No se encontraron noticias para "{{ termino }}".
            </div>

            <ul v-else-if="resultados.length > 0" class="list-unstyled">
              <li
                v-for="noticia in resultados"
                :key="noticia.id"
                class="d-flex align-items-center gap-3 py-2 border-bottom links-search"
                @click="irADetalle(noticia.slug)"
                style="cursor: pointer;"
              >
                <div>
                  <h2 class="fw-bold mb-0 fs-5">{{ noticia.titulo }}</h2>
                  <p class="small mb-0">{{ noticia.resumen }}</p>
                </div>
                <img
                  :src="useMediaUrl(noticia.imagen_portada)"
                  :alt="noticia.imagen_portada_alt"
                  style="width: 100px; height: 60px; object-fit: cover;"
                />
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.search-overlay {
  position: fixed;
  inset: 0;
  z-index: 1050;
  background: #fff;
  overflow: hidden;
}

.result-item:hover {
  background-color: #f8f9fa;
}
</style>