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
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_active and Shift.objects.filter(is_active=True).exists():
            raise ValueError("Solo se puede tener una caja activa a la vez.")
        super().save(*args, **kwargs)

    def close_shift(self, total_income, closed_by):
        self.total_income = total_income
        self.close_time = now()
        self.is_active = False
        self.closed_by = closed_by
        self.save()
