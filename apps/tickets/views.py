from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer
from apps.tariffs.models import Tariff


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.filter(status=1)
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def entrada(self, request):
        vehicle_plate = request.data.get('vehicle_plate')
        user = request.user
        ticket = Ticket.objects.create(vehicle_plate=vehicle_plate, generated_by=user)
        return Response(ticket.generate_entry_ticket(), status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def salida(self, request):
        ticket_number = request.data.get('ticket_number')
        tarifa_id = request.data.get('tarifa_id')
        valor_otros = request.data.get('valor_otros', 0)

        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
            ticket.exit_time = now()
            tarifa = Tariff.objects.get(id=tarifa_id)
            ticket.save()
            return Response(ticket.generate_exit_ticket(tarifa, valor_otros), status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({"error": "Ticket no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Tariff.DoesNotExist:
            return Response({"error": "Tarifa no encontrada"}, status=status.HTTP_404_NOT_FOUND)
