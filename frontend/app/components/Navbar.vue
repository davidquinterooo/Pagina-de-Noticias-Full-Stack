<template>
  <nav class="navbar navbar-expand-lg flex-wrap">
    <div
      class="container-fluid d-flex flex-wrap align-items-center justify-content-between"
    >
      <!-- ================= FILA 1 (ARRIBA) ================= -->
      <!-- Nombre a la izquierda (Ocupa su espacio libre) -->
      <a class="navbar-brand fs-2" href="#">Name Page</a>

      <!-- Redes Sociales a la derecha (Fuera del menú colapsable para que no se mezclen) -->
      <!-- 'ms-auto' las empuja a la derecha, 'd-none d-lg-flex' las oculta en móviles y las muestra en escritorio -->
      <ul class="navbar-nav ms-auto flex-row gap-2 d-none d-lg-flex">
        <li class="nav-item">
          <a
            class="nav-link icons-social d-inline-flex align-items-center"
            href="#"
          >
            <BootstrapIcon name="facebook" />
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link icons-social d-inline-flex align-items-center"
            href="#"
          >
            <BootstrapIcon name="instagram" />
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link icons-social d-inline-flex align-items-center"
            href="#"
          >
            <BootstrapIcon name="twitter-x" />
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link icons-social d-inline-flex align-items-center"
            href="#"
          >
            <BootstrapIcon name="youtube" />
          </a>
        </li>
      </ul>

      <!-- Botón de menú (Se alinea a la derecha automáticamente en móviles gracias a flexbox) -->
      <button
        class="navbar-toggler fs-6 border-0 shadow-none"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
        @click="isMenuOpen = !isMenuOpen"
      >
        <!-- Si el menú está cerrado, muestra las tres líneas -->
        <BootstrapIcon class="icono-navbar" v-if="!isMenuOpen" name="list" />
        <!-- Si el menú está abierto, muestra la "X" para cerrar -->
        <BootstrapIcon class="icono-navbar" v-else name="x-lg" />
      </button>

      <!-- ================= FILA 2 (ABAJO) ================= -->
      <!-- Cambiado: 'w-100' obliga a este bloque a bajar e iniciar una nueva línea limpia -->
      <div class="collapse navbar-collapse w-100" 
      :class="{ 'show': isMenuOpen }"
      id="navbarNav">
        <!-- Las opciones principales se extienden horizontalmente abajo -->
        <!-- 'border-top mt-2 pt-2' crea la separación visual entre la fila superior y el menú -->
        <ul class="navbar-nav w-100 nav-justified text-center">
          <li class="nav-item">
            <a class="nav-link active opcions-navbar" href="#">Options 1</a>
          </li>
          <li class="nav-item">
            <a class="nav-link opcions-navbar" href="#">Options 2</a>
          </li>
          <li class="nav-item">
            <a class="nav-link opcions-navbar" href="#">Options 3</a>
          </li>
          <li class="nav-item">
            <a class="nav-link opcions-navbar" href="#">Options 4</a>
          </li>

          <!-- Duplicado de redes oculto: En móviles aparecerán abajo del menú de forma limpia -->
          <div
            class="d-flex d-lg-none gap-2 justify-content-center"
          >
            <a class="nav-link icons-social" href="#"
              ><BootstrapIcon name="facebook"
            /></a>
            <a class="nav-link icons-social" href="#"
              ><BootstrapIcon name="instagram"
            /></a>
            <a class="nav-link icons-social" href="#"
              ><BootstrapIcon name="twitter-x"
            /></a>
            <a class="nav-link icons-social" href="#"
              ><BootstrapIcon name="youtube"
            /></a>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
// Esta variable controla si el menú está abierto o cerrado 
const isMenuOpen = ref(false)
</script>
