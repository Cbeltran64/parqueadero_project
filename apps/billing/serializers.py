from rest_framework import serializers
from .models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id', 'vehicle', 'tariff', 'entry_time', 'exit_time', 'total_time', 'amount_paid', 'created_at']
