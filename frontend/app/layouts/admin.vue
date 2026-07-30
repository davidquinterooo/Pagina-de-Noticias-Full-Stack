<script setup lang="ts">
const { logout } = useAuth()
</script>

<template>
  <div class="admin-layout">
    <aside class="admin-sidebar">
      <h2 class="fs-4 fw-bold mb-4">Panel de administración</h2>
      <nav class="d-flex flex-column gap-2">
        <NuxtLink to="/admin">Noticias</NuxtLink>
        <NuxtLink to="/admin/noticias/nueva">+ Nueva noticia</NuxtLink>
        <button class="btn btn-link text-start p-0" @click="logout">Cerrar sesión</button>
      </nav>
    </aside>
    <main class="admin-content">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.admin-layout{ 
    display: flex; 
    min-height: 100vh; 
}
.admin-sidebar { 
    width: 220px; 
    padding: 1.5rem; 
    background: #f8f9fa; 
    border-right: 1px solid #dee2e6; 
}
.admin-content { 
    flex: 1; 
    padding: 2rem; 
}
</style>