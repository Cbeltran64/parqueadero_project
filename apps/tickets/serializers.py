from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_number', 'vehicle_plate', 'entry_time', 'exit_time', 'generated_by', 'status']
