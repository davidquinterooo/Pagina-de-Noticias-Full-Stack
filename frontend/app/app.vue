<template>
  <div>
    <!-- Renderizamos el Layout Maestro global -->
    <NuxtLayout>
      <!-- NuxtPage se encarga de cargar los archivos dentro de la carpeta /pages -->
      <NuxtPage />
    </NuxtLayout>
    <SearchOverlay />
  </div>
</template>
