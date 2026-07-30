export const useNoticiasAdmin = () => {
  const { apiFetch } = useApi()

  const getNoticiasAdmin = (params: { page?: number } = {}) => {
    return apiFetch<NoticiasResponse>('/noticias/', { params })
  }

  const getNoticiaAdmin = (slug: string) => {
    return apiFetch<Noticia>(`/noticias/${slug}/`)
  }

  const crearNoticia = (formData: FormData) => {
    return apiFetch<Noticia>('/noticias/', { method: 'POST', body: formData })
  }

  const actualizarNoticia = (slug: string, formData: FormData) => {
    return apiFetch<Noticia>(`/noticias/${slug}/`, { method: 'PATCH', body: formData })
  }

  const eliminarNoticia = (slug: string) => {
    return apiFetch(`/noticias/${slug}/`, { method: 'DELETE' })
  }

    return { getNoticiasAdmin, getNoticiaAdmin, crearNoticia, actualizarNoticia, eliminarNoticia }
}