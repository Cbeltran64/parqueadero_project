from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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

            # Obtener vehículos que aún no han salido
            pending_vehicles = shift.get_pending_vehicles()
            pending_vehicles_serializer = VehicleSerializer(pending_vehicles, many=True)

            # Obtener vehículos que entraron durante el turno
            vehicles_in_shift = shift.get_vehicles_in_shift()
            vehicles_in_shift_serializer = VehicleSerializer(vehicles_in_shift, many=True)

            report = {
                "total_income": shift.total_income,
                "vehicles_in_shift": vehicles_in_shift_serializer.data,
                "pending_vehicles": pending_vehicles_serializer.data,
            }

            return Response({"status": "Turno cerrado correctamente.", "report": report}, status=status.HTTP_200_OK)
        except Shift.DoesNotExist:
            return Response({"error": "Turno no encontrado."}, status=status.HTTP_404_NOT_FOUND)
