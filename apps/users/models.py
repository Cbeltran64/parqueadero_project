from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Eliminar el campo 'role'
    # Añadir campos booleanos para las opciones del menú
    gestion_usuarios = models.BooleanField(default=False)
    configuracion_sistema = models.BooleanField(default=False)
    generacion_reportes = models.BooleanField(default=False)
    sistema = models.BooleanField(default=False)

    def __str__(self):
        return self.username
