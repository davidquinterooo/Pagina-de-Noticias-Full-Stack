<script setup lang="ts">
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { watch } from 'vue'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{ (e: 'update:modelValue', value: string): void }>()

const editor = useEditor({
  content: props.modelValue,
  extensions: [StarterKit],
  onUpdate: ({ editor }) => emit('update:modelValue', editor.getHTML()),
})

watch(() => props.modelValue, (nuevoValor) => {
  if (editor.value && nuevoValor !== editor.value.getHTML()) {
    editor.value.commands.setContent(nuevoValor, false)
  }
})

onBeforeUnmount(() => editor.value?.destroy())
</script>

<template>
  <div class="rich-text-editor">
    <div class="toolbar mb-2 d-flex gap-2">
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="editor?.chain().focus().toggleBold().run()"><b>B</b></button>
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="editor?.chain().focus().toggleItalic().run()"><i>I</i></button>
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="editor?.chain().focus().toggleHeading({ level: 2 }).run()">H2</button>
      <button type="button" class="btn btn-sm btn-outline-secondary" @click="editor?.chain().focus().toggleBulletList().run()">• Lista</button>
    </div>
    <EditorContent :editor="editor" class="border rounded p-3" style="min-height: 250px;" />
  </div>
</template>