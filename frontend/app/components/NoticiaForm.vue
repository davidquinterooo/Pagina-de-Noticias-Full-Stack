<script setup lang="ts">
import { ref } from 'vue'
const props = defineProps<{ noticia?: any }>()
const emit = defineEmits<{ (e: 'submit', formData: FormData): void }>()

const titulo = ref(props.noticia?.titulo ?? '')
const resumen = ref(props.noticia?.resumen ?? '')
const contenido = ref(props.noticia?.contenido ?? '')
const estado = ref(props.noticia?.estado ?? 'borrador')
const imagenAlt = ref(props.noticia?.imagen_portada_alt ?? '')
const archivoImagen = ref<File | null>(null)

const onFileChange = (e: Event) => {
  archivoImagen.value = (e.target as HTMLInputElement).files?.[0] ?? null
}

const onSubmit = () => {
  const formData = new FormData()
  formData.append('titulo', titulo.value)
  formData.append('resumen', resumen.value)
  formData.append('contenido', contenido.value)
  formData.append('estado', estado.value)
  formData.append('imagen_portada_alt', imagenAlt.value)
  if (archivoImagen.value) {
    formData.append('imagen_portada', archivoImagen.value)
  }
  emit('submit', formData)
}
</script>

<template>
  <form @submit.prevent="onSubmit">
    <div class="mb-3">
      <label class="form-label">Título</label>
      <input v-model="titulo" type="text" class="form-control" required />
    </div>

    <div class="mb-3">
      <label class="form-label">Resumen</label>
      <textarea v-model="resumen" class="form-control" rows="2" maxlength="300" required></textarea>
    </div>

    <div class="mb-3">
      <label class="form-label">Contenido</label>
      <RichTextEditor v-model="contenido" />
    </div>

    <div class="mb-3">
      <label class="form-label">Imagen de portada</label>
      <input
        type="file"
        accept="image/*"
        class="form-control"
        :required="!noticia?.imagen_portada"
        @change="onFileChange"
      />
      <small v-if="noticia?.imagen_portada" class="text-muted">
        Ya hay una imagen cargada. Sube una nueva solo si quieres reemplazarla.
      </small>
    </div>

    <div class="mb-3">
      <label class="form-label">Texto alternativo de la imagen</label>
      <input v-model="imagenAlt" type="text" class="form-control" />
    </div>

    <div class="mb-3">
      <label class="form-label">Estado</label>
      <select v-model="estado" class="form-select">
        <option value="borrador">Borrador</option>
        <option value="publicado">Publicado</option>
      </select>
    </div>

    <button type="submit" class="btn btn-dark">Guardar</button>
  </form>
</template>