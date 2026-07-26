from rest_framework import permissions

class EsAdminOSoloLectura(permissions.BasePermission):
    """
    Cualquiera puede leer (GET/HEAD/OPTIONS).
    Solo un usuario autenticado (el admin) puede crear/editar/eliminar.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated