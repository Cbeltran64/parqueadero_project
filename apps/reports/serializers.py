from rest_framework import serializers
from apps.billing.models import Billing
from apps.vehicles.models import Vehicle

class ReportSerializer(serializers.Serializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate')
    vehicle_type = serializers.CharField(source='vehicle.vehicle_type')
    entry_time = serializers.DateTimeField()
    exit_time = serializers.DateTimeField()
    amount_paid = serializers.DecimalField(max_digits=10, decimal_places=2)
    tariff_name = serializers.CharField(source='tariff.name')
