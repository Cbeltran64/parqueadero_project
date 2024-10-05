# models.py

from django.db import models
from apps.users.models import CustomUser
from apps.tickets.models import Ticket

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Carro'),
        ('motorcycle', 'Moto'),
        ('car_student', 'Carro Estudiante'),
        ('motorcycle_student', 'Moto Estudiante'),
    ]

    plate = models.CharField(max_length=10, unique=True, db_index=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    registered_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def soft_delete(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return f"Vehículo {self.plate} - {self.vehicle_type}"
