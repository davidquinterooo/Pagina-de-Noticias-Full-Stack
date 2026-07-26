# Contexto de debugging: error TSCONFIG_ERROR en Vite/Nuxt

## Objetivo
Encontrar la causa raíz y solucionar un error de Vite que impide cargar páginas dentro de `frontend/app/pages/noticias/`, para poder restaurar una ruta dinámica de detalle de noticia (`/noticias/[slug]`).

## Stack y versiones (confirmado con `npx nuxi info`)
- Windows 10.0.19045
- Node.js v22.19.0
- nuxt/cli 3.37.0
- Nuxt 4.4.8
- Nitro 2.13.4
- Vite 7.3.6 (builder)
- Vue 3.5.40
- Módulos: @pinia/nuxt@1.0.1, @nuxt/image@2.0.0, nuxt-bootstrap-icons@3.3.3
- Package manager: npm@10.9.3
- Estructura del proyecto: Nuxt 4 con todo dentro de `frontend/app/` (app/pages, app/components, app/composables, app/layouts, app/app.vue)

## Error exacto

```
[TSCONFIG_ERROR] Failed to load tsconfig for 'app/pages/noticias/detalle.vue': Tsconfig not found
```

Ocurre durante `transformWithOxc` (el nuevo motor de transformación de Vite 7), al intentar compilar cualquier archivo `.vue` que esté dentro de `app/pages/noticias/` (una subcarpeta de `pages/`). Archivos directamente en `app/pages/` (como `index.vue`) SÍ cargan bien.

## Cronología de lo intentado (en orden)

1. **Archivo original**: `app/pages/noticias/[slug].vue` → daba el mismo error `TSCONFIG_ERROR: Tsconfig not found`.
2. **Se revisó `frontend/tsconfig.json`**: tenía un error real de JSON (una entrada `{"extends": "..."}` mezclada dentro del array `references`, que solo debe contener objetos `{"path": "..."}`). Se corrigió a la estructura estándar de Nuxt 4 (archivo "solution-style", solo con `references` a los tsconfig generados en `.nuxt/`). Esto solucionó un primer error de parseo JSON, pero el error de `Tsconfig not found` volvió a aparecer después.
3. **Se renombró el archivo** a `app/pages/noticias/detalle.vue` (sin corchetes) → cargó bien. Esto hizo sospechar que el problema eran los corchetes en el nombre de archivo.
4. **Se probó con estructura de carpeta** `app/pages/noticias/[slug]/index.vue` (corchetes en el nombre de la carpeta, no del archivo) → dio el mismo error. Esto descartó que fuera específicamente el nombre del archivo.
5. **Se implementó un workaround** con el hook `pages:extend` en `nuxt.config.ts`, para registrar la ruta dinámica manualmente apuntando a `detalle.vue` (sin corchetes en el path físico) usando `fileURLToPath(new URL(...))`. Esto rompió TODAS las páginas del proyecto (incluyendo `index.vue`, que antes cargaba bien) con el mismo error `Tsconfig not found`.
6. **Se comentó el hook `pages:extend`** por completo → el error persistió en `detalle.vue`, y ya NO se restauró el comportamiento original en el que `index.vue` cargaba bien pero `detalle.vue` no. (No está claro si `index.vue` sigue funcionando en este estado; falta confirmar.)
7. **Se verificó que no hay archivos residuales** con corchetes en `app/pages/noticias/` (`dir` mostró solo `detalle.vue`, limpio).
8. **Hipótesis actual sin confirmar**: el `tsconfig.json` raíz de `frontend/` es "solution-style" (solo contiene `references` a los tsconfig generados en `.nuxt/`, sin `compilerOptions` propias). El motor `oxc` de Vite 7 podría estar fallando al resolver esas referencias para archivos ubicados en subcarpetas de `pages/` (profundidad > 1 dentro de `app/`), aunque esto no está confirmado, solo es la hipótesis que se estaba por probar.
9. **Último paso sugerido (no confirmado si se aplicó)**: crear `frontend/app/tsconfig.json` con:
   ```json
   {
     "extends": "../.nuxt/tsconfig.app.json"
   }
   ```
   para darle a los archivos dentro de `app/` un tsconfig con `compilerOptions` reales y no depender de la resolución de `references`.

## `frontend/tsconfig.json` actual (raíz, corregido en el paso 2)

```json
{
  "files": [],
  "references": [
    { "path": "./.nuxt/tsconfig.app.json" },
    { "path": "./.nuxt/tsconfig.server.json" },
    { "path": "./.nuxt/tsconfig.shared.json" },
    { "path": "./.nuxt/tsconfig.node.json" }
  ]
}
```

## Estado actual del `nuxt.config.ts`

El bloque `hooks: { 'pages:extend': ... }` está comentado. El resto de la config:

```ts
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  modules: ["@pinia/nuxt", "@nuxt/image", "nuxt-bootstrap-icons"],
  css: ["~/assets/css/main.css", "bootstrap/dist/css/bootstrap.min.css"],
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE,
      mediaBase: process.env.NUXT_PUBLIC_MEDIA_BASE,
    },
  },
})
```

## Cosas que NO se han probado todavía

- Confirmar si con el hook comentado, `index.vue` (en la raíz de `pages/`) sigue cargando bien mientras `detalle.vue` (en la subcarpeta `pages/noticias/`) falla — para aislar si el problema es específicamente "profundidad de carpeta" o algo distinto que se rompió en el paso 5-6.
- Probar downgrade de Vite a una versión anterior a la 7.x (donde no exista el motor `oxc` para tsconfig) para confirmar si es un bug de esa versión específica.
- Revisar si el `.nuxt/tsconfig.app.json` generado realmente incluye `app/pages/noticias/**/*` en su `include` (se confirmó una vez que sí decía `"../app/**/*"`, pero convendría re-verificar después de todos los cambios).
- Probar crear `frontend/app/tsconfig.json` con `extends` hacia `.nuxt/tsconfig.app.json` (paso 9, sugerido pero no confirmado si se ejecutó).
- Revisar si hay algún `.gitignore`/exclude o algún otro `tsconfig.json` suelto en el proyecto (por ejemplo dentro de `app/`) que esté interfiriendo.

## Objetivo final

1. Encontrar la causa raíz exacta del `TSCONFIG_ERROR: Tsconfig not found` para archivos dentro de subcarpetas de `app/pages/`.
2. Restaurar una ruta dinámica funcional para el detalle de noticias: `/noticias/:slug` debe cargar un componente Vue que reciba el `slug` desde `useRoute().params.slug`, consumiendo el backend Django (`GET http://localhost:8000/api/noticias/{slug}/`).
3. Preferiblemente usando la convención estándar de Nuxt (`app/pages/noticias/[slug].vue` o `app/pages/noticias/[slug]/index.vue`), a menos que se confirme que eso es imposible en este entorno, en cuyo caso usar el workaround del hook `pages:extend` corregido (con una construcción de ruta de archivo que sí funcione en Windows).

## Contexto adicional del proyecto (para orientar, no directamente relacionado al bug)

- Backend: Django + DRF corriendo en `http://localhost:8000`, con endpoint `GET /api/noticias/{slug}/`.
- Frontend: Nuxt 3/4 + Bootstrap + Pinia + TipTap.
- Composables ya creados: `useApi.ts`, `useNoticias.ts`, `useMediaUrl.ts` — funcionando correctamente (no están relacionados al bug).
- El componente `detalle.vue` (contenido actual, sin corchetes en el nombre) es el que se intenta cargar en `/noticias/detalle` como prueba, antes de restaurar el parámetro dinámico real.
