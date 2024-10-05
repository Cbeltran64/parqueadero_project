from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.filter(status=1)  # Solo mostrar tiquetes activos
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Código existente para crear un tiquete
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(generated_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Código existente para actualizar un tiquete
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Elimina lógicamente el tiquete."""
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def print(self, request, pk=None):
        """Obtener información detallada del tiquete para impresión."""
        ticket = self.get_object()
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)