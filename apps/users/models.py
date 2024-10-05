from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('oper_admin', 'Operario Administrador'),
        ('oper_employee', 'Operador Empleado'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)  # Cambiar a False en lugar de eliminar

    # Especificar un related_name para evitar conflictos con el modelo User de Django
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Cambia el related_name para evitar colisiones
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Cambia el related_name para evitar colisiones
        blank=True,
        help_text='Permisos específicos del usuario.'
    )

    def soft_delete(self):
        """Realiza una eliminación lógica cambiando el estado a inactivo."""
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username

