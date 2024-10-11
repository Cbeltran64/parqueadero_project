from rest_framework import serializers
from .models import Tariff, Convenio

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['id', 'nombre_tarifa', 'vehicle_type', 'price_per_minute', 'convenio']

    def validate_price_per_minute(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("El cobro por minuto debe ser un número positivo.")
        return value

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ['id', 'nombre_convenio', 'porcentaje_descuento']

    def validate_porcentaje_descuento(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("El porcentaje de descuento debe estar entre 0 y 100.")
        return value

    def calcular_costo(self, tiempo_estancia):
        total_minutos = tiempo_estancia.total_seconds() / 60
        costo = total_minutos * self.price_per_minute if self.price_per_minute else 0

        if self.convenio:
            descuento = (self.convenio.porcentaje_descuento / 100) * costo
            costo -= descuento

        return round(costo, 2)