from rest_framework.permissions import BasePermission

class HasConfiguracionSistemaPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.configuracion_sistema
