from django.contrib import admin
from .models import Billing

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'tariff', 'entry_time', 'exit_time', 'total_time', 'amount_paid', 'created_at')
    search_fields = ('vehicle__plate',)
    list_filter = ('tariff', 'created_at')
