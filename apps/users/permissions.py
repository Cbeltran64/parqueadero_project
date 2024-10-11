from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOperAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or (
            request.user.role == 'oper_admin' and view.action in ['retrieve', 'list']
        )
