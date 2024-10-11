from django.db import models

class Convenio(models.Model):
    nombre_convenio = models.CharField(max_length=100, unique=True)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_convenio

class Tariff(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Carro'),
        ('motorcycle', 'Moto'),
        ('bicycle', 'Bicicleta'),
    ]

    nombre_tarifa = models.CharField(max_length=100, unique=True, default='Tarifa Genérica')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    price_per_minute = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarifas')

    def __str__(self):
        return f"{self.nombre_tarifa} - {self.vehicle_type}"

    class Meta:
        verbose_name = "Tarifa"
        verbose_name_plural = "Tarifas"
