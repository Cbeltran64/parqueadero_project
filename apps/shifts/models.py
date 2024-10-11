from django.db import models
from apps.users.models import CustomUser
from django.utils.timezone import now
from apps.vehicles.models import Vehicle

class Shift(models.Model):
    opened_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="shifts_opened")
    closed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="shifts_closed", blank=True)
    open_time = models.DateTimeField(auto_now_add=True)
    close_time = models.DateTimeField(null=True, blank=True)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)  # Indica si el turno está activo o cerrado
    vehicles = models.ManyToManyField(Vehicle, blank=True)  # Relación con los vehículos del turno

    def close_shift(self, total_income, closed_by):
        """Cerrar el turno actual y registrar el total de ingresos"""
        self.total_income = total_income
        self.close_time = now()
        self.is_active = False
        self.closed_by = closed_by
        self.save()

    def get_pending_vehicles(self):
        """Obtener vehículos que aún no han salido"""
        return self.vehicles.filter(exit_time__isnull=True)

    def __str__(self):
        return f"Turno abierto por {self.opened_by} - Estado: {'Abierto' if self.is_active else 'Cerrado'}"
