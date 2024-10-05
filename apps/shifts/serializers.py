from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['opened_by', 'closed_by', 'open_time', 'close_time', 'total_income', 'is_active']
