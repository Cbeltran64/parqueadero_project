from django.contrib import admin
from .models import Shift

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('opened_by', 'closed_by', 'open_time', 'close_time', 'total_income', 'is_active')
    list_filter = ('is_active', 'open_time', 'close_time')
    search_fields = ('opened_by__username', 'closed_by__username')
