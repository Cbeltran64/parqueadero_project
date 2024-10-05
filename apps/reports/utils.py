import csv
from io import StringIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_csv_report(data):
    """Genera un reporte en formato CSV"""
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Placa', 'Tipo de vehículo', 'Hora de entrada', 'Hora de salida', 'Monto pagado', 'Tarifa'])

    for item in data:
        writer.writerow([
            item['vehicle_plate'],
            item['vehicle_type'],
            item['entry_time'],
            item['exit_time'],
            item['amount_paid'],
            item['tariff_name'],
        ])

    output.seek(0)
    response = HttpResponse(output, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=report.csv'
    return response


def generate_pdf_report(data):
    """Genera un reporte en formato PDF"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=report.pdf'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Reporte de Ventas - Parqueadero")
    p.drawString(100, 730, "Placa | Tipo de Vehículo | Entrada | Salida | Monto Pagado | Tarifa")

    y_position = 710
    for item in data:
        p.drawString(100, y_position,
                     f"{item['vehicle_plate']} | {item['vehicle_type']} | {item['entry_time']} | {item['exit_time']} | {item['amount_paid']} | {item['tariff_name']}")
        y_position -= 20

    p.showPage()
    p.save()
    return response
