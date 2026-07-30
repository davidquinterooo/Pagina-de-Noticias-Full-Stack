export const useAuth = () => {
    const { apiFetch } = useApi()

    const token = useCookie<string | null>('access_token', {
        maxAge: 60 * 60 * 8, // 8 horas, igual al access token del backend
        sameSite: 'lax',
    })

    const isLoggedIn = computed(() => !!token.value)

    const login = async (username: string, password: string) => {
        const data = await apiFetch<{ access: string; refresh: string }>('/auth/login/', {
        method: 'POST',
        body: { username, password },
        })
        token.value = data.access
    }

    const logout = () => {
        token.value = null
        navigateTo('/admin/login')
    }

    return { token, isLoggedIn, login, logout }
}
