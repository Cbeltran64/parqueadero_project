from django.contrib import admin
from .models import Tariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'price_per_minute', 'fixed_price', 'max_duration_fixed')
    list_filter = ('vehicle_type',)
    search_fields = ('name',)
