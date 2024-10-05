from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.filter(is_active=True)
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Código existente para crear un vehículo
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(registered_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Código existente para actualizar un vehículo
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Elimina lógicamente un vehículo."""
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
