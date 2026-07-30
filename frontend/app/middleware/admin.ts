export default defineNuxtRouteMiddleware((to) => {
  if (to.path === "/admin/login") return;

  const token = useCookie("access_token");
  if (!token.value) {
    return navigateTo("/admin/login");
  }
});
