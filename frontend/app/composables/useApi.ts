export const useApi = () => {
  const config = useRuntimeConfig()
  const token = useCookie<string | null>('access_token')

  const apiFetch = $fetch.create({
    baseURL: config.public.apiBase,
    onRequest({ options }) {
      if (token.value) {
        options.headers = new Headers(options.headers)
        options.headers.set('Authorization', `Bearer ${token.value}`)
      }
    },
    onResponseError({ response }) {
      if (response.status === 401) {
        token.value = null
        navigateTo('/admin/login')
      }
    },
  })

  return { apiFetch }
}