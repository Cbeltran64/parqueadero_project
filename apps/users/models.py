from django.contrib.auth.models import AbstractUser
from django.db import models

class MenuOption(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('oper_admin', 'Operario Administrador'),
        ('oper_employee', 'Operador Empleado'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)  # Cambiar a False en lugar de eliminar
    menu_permissions = models.ManyToManyField(MenuOption, blank=True)

    def soft_delete(self):
        """Realiza una eliminación lógica cambiando el estado a inactivo."""
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username
