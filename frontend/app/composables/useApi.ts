export const useApi = () => {
  const config = useRuntimeConfig()

  const apiFetch = $fetch.create({
    baseURL: config.public.apiBase, // http://localhost:8000/api
  })

  return { apiFetch }
}