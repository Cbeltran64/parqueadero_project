from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now, timedelta
from .serializers import ReportSerializer
from apps.billing.models import Billing
from .utils import generate_csv_report, generate_pdf_report
from rest_framework.permissions import IsAuthenticated

class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, period, format=None):
        """
        period: puede ser 'daily', 'weekly', 'biweekly', o 'monthly'
        """
        # Determinar el periodo de tiempo
        if period == 'daily':
            start_date = now().replace(hour=0, minute=0, second=0)
        elif period == 'weekly':
            start_date = now() - timedelta(days=7)
        elif period == 'biweekly':
            start_date = now() - timedelta(days=14)
        elif period == 'monthly':
            start_date = now() - timedelta(days=30)
        else:
            return Response({"error": "Periodo inválido"}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar facturas por el periodo de tiempo
        billings = Billing.objects.filter(created_at__gte=start_date)

        # Filtrar por tipo de vehículo si se proporciona
        vehicle_type = request.GET.get('vehicle_type')
        if vehicle_type:
            billings = billings.filter(vehicle__vehicle_type=vehicle_type)

        serializer = ReportSerializer(billings, many=True)

        # Generar el reporte según el formato
        report_format = request.GET.get('format')
        if report_format == 'csv':
            csv_report = generate_csv_report(serializer.data)
            return csv_report  # Este método genera el CSV como respuesta HTTP
        elif report_format == 'pdf':
            pdf_report = generate_pdf_report(serializer.data)
            return pdf_report  # Este método genera el PDF como respuesta HTTP
        else:
            return Response(serializer.data)