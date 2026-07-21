<template>
  <Navbar />
  <main class="d-flex flex-nowrap min-vh-100">
    <!-- LADO IZQUIERDO: El contenido de la página de noticias -->
    <!-- flex-grow-1 hace que este div use todo el ancho sobrante de la pantalla -->
    <div class="flex-grow-1 p-4">
      <!-- Si estás en un Layout de Nuxt, aquí va la página actual -->
      <NuxtPage /> 
    </div>
    <!-- LADO DERECHO: Sidebar -->
    <Sidebar />
  </main>
</template>