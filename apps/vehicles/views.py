from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vehicle
from apps.shifts.models import Shift
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.filter(is_active=True)
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Obtener el turno activo
        try:
            turno_actual = Shift.objects.get(is_active=True)
        except Shift.DoesNotExist:
            return Response({"error": "No hay un turno abierto actualmente."}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el vehículo y asociarlo al turno activo
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle = serializer.save(registered_by=request.user)

        turno_actual.vehicles.add(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
