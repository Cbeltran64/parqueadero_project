from django.contrib import admin
from .models import CustomUser, MenuOption

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
    filter_horizontal = ('menu_permissions',)  # Permitir seleccionar múltiples permisos fácilmente

@admin.register(MenuOption)
class MenuOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)
