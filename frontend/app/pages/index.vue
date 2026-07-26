<!-- <template>
  <div class="container">
    <ul class="list-unstyled p-0 row gx-2 gy-5 justify-content-evenly">
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
      <li class="col-12 col-sm-6 col-md-auto">
        <div class="card-hover w-100" style="max-width: 17rem;">
          <a class="links-card" href="https://www.google.com" style="text-decoration: none;">
            <img 
              src="/portadahd.jpg" 
              class="card-img-top w-100" 
              alt="..."
              style="height: 160px; object-fit: cover; border-radius: 5px;"
            >
            <p class="fs-5 lh-1 fw-bold mt-2">
              Some quick example text to build on the card title and make up the bulk of the card’s content.
            </p>
          </a>        
        </div>
      </li>
    </ul>
  </div>
</template> -->

<script setup lang="ts">
const { getNoticias } = useNoticias();
const page = ref(1);

const { data, status, error, refresh } = await useAsyncData(
  () => `noticias-page-${page.value}`,
  () => getNoticias({ page: page.value }),
  { default: () => ({ count: 0, next: null, previous: null, results: [] }) }
)

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
