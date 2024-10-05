from django.db import models
from apps.users.models import CustomUser  # Importa el modelo de usuario

class Ticket(models.Model):
    STATUS_CHOICES = [
        (1, 'Activo'),
        (0, 'Inactivo'),
    ]

    ticket_number = models.AutoField(primary_key=True)
    vehicle_plate = models.CharField(max_length=10)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    generated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def soft_delete(self):
        """Elimina lógicamente el tiquete cambiando su estado a inactivo."""
        self.status = 0
        self.save()

    def __str__(self):
        return f"Tiquete {self.ticket_number} - Vehículo {self.vehicle_plate}"

    class Meta:
        verbose_name = "Tiquete"
        verbose_name_plural = "Tiquetes"