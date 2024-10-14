from django.db import models
from django.contrib.postgres.fields import JSONField

class ParkingInfo(models.Model):
    nombre_parqueadero = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    poliza = models.CharField(max_length=100)
    fecha_vencimiento_poliza = models.DateField(null=True, blank=True)
    horario_atencion = models.CharField(max_length=250, null=True, blank=True)
    atencion_cliente = models.CharField(max_length=200)
    capacidad_espacios = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_parqueadero
