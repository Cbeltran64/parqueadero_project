from django.db import models
from apps.vehicles.models import Vehicle
from apps.tariffs.models import Tariff

class Billing(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    total_time = models.DurationField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_time(self):
        """Calcula el tiempo total de estancia basado en la hora de entrada y salida."""
        if self.exit_time:
            self.total_time = self.exit_time - self.entry_time
            self.save()

    def calculate_amount_paid(self):
        """Calcula el monto total a pagar basado en la tarifa y el tiempo total."""
        if self.total_time and self.tariff:
            total_minutes = self.total_time.total_seconds() / 60
            if self.tariff.price_per_minute:
                self.amount_paid = total_minutes * self.tariff.price_per_minute
            elif self.tariff.fixed_price:
                self.amount_paid = self.tariff.fixed_price
            self.save()

    def __str__(self):
        return f"Factura para el vehículo {self.vehicle.plate} - Total Pagado: {self.amount_paid}"
