from django.db import models

class ParkingInfo(models.Model):
    nombre_parqueadero = models.CharField(max_length=100)
    nit = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    poliza = models.CharField(max_length=100)
    fecha_vencimiento_poliza = models.DateField()
    horario_atencion = models.JSONField()
    atencion_cliente = models.CharField(max_length=100)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_parqueadero
