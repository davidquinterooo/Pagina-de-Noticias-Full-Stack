<template>
  <Navbar />
  <main class="d-flex flex-nowrap min-vh-100">
    <!-- LADO IZQUIERDO: El contenido de la página de noticias -->
    <!-- flex-grow-1 hace que este div use todo el ancho sobrante de la pantalla -->
    <div class="flex-grow-1 pt-3">
      <NuxtPage /> 
    </div>
    <!-- LADO DERECHO: Sidebar -->
    <Sidebar />
  </main>
  <Footer />
</template>