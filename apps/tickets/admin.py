from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'vehicle_plate', 'entry_time', 'exit_time', 'status')
    list_filter = ('status', 'entry_time', 'exit_time')
    search_fields = ('vehicle_plate', 'ticket_number')
