export const useMediaUrl = (path: string) => {
  if (!path) return "";

  // Si el backend ya mandó una URL absoluta (con http:// o https://), úsala tal cual
  if (path.startsWith("http://") || path.startsWith("https://")) {
    return path;
  }

  // Si mandó una ruta relativa, arma la URL completa
  const config = useRuntimeConfig();
  return `${config.public.mediaBase}${path}`;
};
