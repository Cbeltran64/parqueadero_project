from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'gestion_usuarios', 'configuracion_sistema',
                'generacion_reportes', 'sistema'
            ),
        }),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
