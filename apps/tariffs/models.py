from django.db import models

class Tariff(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Carro'),
        ('motorcycle', 'Moto'),
        ('car_student', 'Carro Estudiante'),
        ('motorcycle_student', 'Moto Estudiante'),
    ]

    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    price_per_minute = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fixed_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    max_duration_fixed = models.PositiveIntegerField(null=True, blank=True, help_text="Duración máxima (en horas) para tarifas fijas")

    def __str__(self):
        return f"{self.name} - {self.vehicle_type}"

    class Meta:
        verbose_name = "Tarifa"
        verbose_name_plural = "Tarifas"
