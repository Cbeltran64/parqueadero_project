from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'plate', 'vehicle_type', 'entry_time', 'exit_time', 'ticket', 'registered_by']
