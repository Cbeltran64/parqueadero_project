from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'oper_admin']
