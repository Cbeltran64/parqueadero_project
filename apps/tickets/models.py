from apps.parkinginfo.models import ParkingInfo
from apps.users.models import CustomUser
from datetime import timedelta
from django.db import models

class Ticket(models.Model):
    ticket_number = models.AutoField(primary_key=True)
    vehicle_plate = models.CharField(max_length=10)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    generated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1)

    def soft_delete(self):
        """Elimina lógicamente el tiquete cambiando su estado a inactivo."""
        self.status = 0
        self.save()

    def generate_entry_ticket(self):
        parking_info = ParkingInfo.objects.first()  # Obtener la información del parqueadero
        return {
            "nombre_parqueadero": parking_info.nombre_parqueadero,
            "direccion": parking_info.direccion,
            "telefono": parking_info.telefono,
            "ticket_number": self.ticket_number,
            "vehicle_plate": self.vehicle_plate,
            "entry_time": self.entry_time.strftime('%H:%M - %d %b %y'),
            "generated_by": self.generated_by.username if self.generated_by else 'N/A',
            "poliza": parking_info.poliza,
            "fecha_vencimiento_poliza": parking_info.fecha_vencimiento_poliza.strftime('%d-%m-%Y'),
            "atencion_cliente": parking_info.atencion_cliente,
            "horario_atencion": parking_info.horario_atencion,
            "mensaje_adicional": "Guarde este Tiquete en lugar seguro y entréguelo para retirar el Vehículo. La pérdida del Tiquete tiene un costo de $3,000.00",
            "bienvenida": "BIENVENIDO"
        }

    def generate_exit_ticket(self, tarifa, valor_otros=0):
        parking_info = ParkingInfo.objects.first()  # Obtener la información del parqueadero
        tiempo_estadia = self.exit_time - self.entry_time
        total_minutos = tiempo_estadia.total_seconds() / 60
        valor_tarifa = total_minutos * tarifa.price_per_minute if tarifa.price_per_minute else 0
        valor_total = valor_tarifa + valor_otros

        return {
            "nombre_parqueadero": parking_info.nombre_parqueadero,
            "nit": parking_info.nit,
            "direccion": parking_info.direccion,
            "telefono": parking_info.telefono,
            "factura_numero": self.ticket_number,
            "vehicle_plate": self.vehicle_plate,
            "entry_time": self.entry_time.strftime('%H:%M - %d %b %y'),
            "exit_time": self.exit_time.strftime('%H:%M - %d %b %y'),
            "tiempo_estadia": f"{int(total_minutos // 60)} h {int(total_minutos % 60)} min",
            "tarifa_nombre": tarifa.nombre_tarifa,
            "valor_otros": valor_otros,
            "valor_pagado": valor_total,
            "generated_by": self.generated_by.username if self.generated_by else 'N/A',
            "poliza": parking_info.poliza,
            "fecha_vencimiento_poliza": parking_info.fecha_vencimiento_poliza.strftime('%d-%m-%Y'),
            "atencion_cliente": parking_info.atencion_cliente,
            "sistema": "ParkGenius"
        }
