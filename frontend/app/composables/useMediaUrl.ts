export const useMediaUrl = (path: string) => {
  const config = useRuntimeConfig()
  if (!path) return ''
  return `${config.public.mediaBase}${path}`
}