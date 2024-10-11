from django.db import models

class ParkingInfo(models.Model):
    nombre_parqueadero = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    poliza = models.CharField(max_length=100)
    fecha_vencimiento_poliza = models.DateField()
    horario_atencion = models.JSONField()  # Contiene los horarios de atención
    atencion_cliente = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)  # URL o path al archivo de imagen
    capacidad_espacios = models.PositiveIntegerField(default=10)  # Añadir un valor predeterminado

    def __str__(self):
        return self.nombre_parqueadero
