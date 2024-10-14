from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Shift
from .serializers import ShiftSerializer
from apps.vehicles.serializers import VehicleSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.gestion_usuarios or user.configuracion_sistema:
            return Shift.objects.all()
        else:
            return Shift.objects.none()

class VehicleCountsInShiftView(APIView):
    def get(self, request):
        try:
            turno_actual = Shift.objects.get(is_active=True)
        except Shift.DoesNotExist:
            return Response({"motos": 0, "carros": 0, "bicicletas": 0}, status=status.HTTP_200_OK)

        # Contar los vehículos de cada tipo en el turno actual
        motos_count = turno_actual.vehicles.filter(vehicle_type='motorcycle', exit_time__isnull=True).count()
        carros_count = turno_actual.vehicles.filter(vehicle_type='car', exit_time__isnull=True).count()
        bicicletas_count = turno_actual.vehicles.filter(vehicle_type='bicycle', exit_time__isnull=True).count()

        data = {
            "motos": motos_count,
            "carros": carros_count,
            "bicicletas": bicicletas_count
        }

        return Response(data, status=status.HTTP_200_OK)