interface Noticia {
  id: number
  titulo: string
  slug: string
  resumen: string
  contenido?: string
  imagen_portada: string
  imagen_portada_alt: string
  fecha_publicacion: string
}

interface NoticiasResponse {
  count: number
  next: string | null
  previous: string | null
  results: Noticia[]
}

export const useNoticias = () => {
  const { apiFetch } = useApi()

  const getNoticias = (params: { page?: number; search?: string } = {}) => {
    return apiFetch<NoticiasResponse>('/noticias/', { params })
  }

  const getNoticiaPorSlug = (slug: string) => {
    return apiFetch<Noticia>(`/noticias/${slug}/`)
  }

  return { getNoticias, getNoticiaPorSlug }
}