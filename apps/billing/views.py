from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Billing
from .serializers import BillingSerializer
from rest_framework.permissions import IsAuthenticated

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.calculate_total_time()
        instance.calculate_amount_paid()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance.calculate_total_time()
        instance.calculate_amount_paid()
        return Response(serializer.data)
