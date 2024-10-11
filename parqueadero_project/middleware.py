from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class PermissionMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user
        if user.is_authenticated and hasattr(view_func, 'view_class'):
            view_class = view_func.view_class
            if hasattr(view_class, 'permission_classes'):
                for permission in view_class.permission_classes:
                    if not permission().has_permission(request, view_class):
                        return JsonResponse({'error': 'No tiene permiso para acceder a este recurso.'}, status=403)
        return None
