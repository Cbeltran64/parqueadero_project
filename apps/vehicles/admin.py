from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'vehicle_type', 'entry_time', 'exit_time', 'ticket', 'registered_by')
    search_fields = ('plate',)
    list_filter = ('vehicle_type', 'entry_time', 'exit_time')
