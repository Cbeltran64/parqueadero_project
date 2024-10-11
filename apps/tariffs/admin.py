from django.contrib import admin
from .models import Tariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('nombre_tarifa', 'vehicle_type', 'price_per_minute', 'convenio')
    list_filter = ('vehicle_type', 'convenio')
    search_fields = ('nombre_tarifa',)
