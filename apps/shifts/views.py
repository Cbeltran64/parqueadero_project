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

    def perform_create(self, serializer):
        """Crear un nuevo turno (apertura de caja)"""
        serializer.save(opened_by=self.request.user)

    def close_shift(self, request, pk=None):
        """Cerrar el turno actual, calculando el total de ingresos"""
        try:
            shift = self.get_object()
            if not shift.is_active:
                return Response({"error": "El turno ya está cerrado."}, status=status.HTTP_400_BAD_REQUEST)

            total_income = request.data.get('total_income')
            if total_income is None:
                return Response({"error": "Debe proporcionar el total de ingresos."}, status=status.HTTP_400_BAD_REQUEST)

            shift.close_shift(total_income=total_income, closed_by=request.user)

            # Generar reporte solo con el total de ingresos
            report = {
                "total_income": shift.total_income,
            }

            return Response({"status": "Turno cerrado correctamente.", "report": report}, status=status.HTTP_200_OK)
        except Shift.DoesNotExist:
            return Response({"error": "Turno no encontrado."}, status=status.HTTP_404_NOT_FOUND)

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