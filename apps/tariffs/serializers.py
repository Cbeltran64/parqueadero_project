from rest_framework import serializers
from .models import Tariff

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['id', 'name', 'vehicle_type', 'price_per_minute', 'fixed_price', 'max_duration_fixed']
