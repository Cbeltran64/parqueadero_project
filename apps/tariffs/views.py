from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tariff, Convenio
from .serializers import TariffSerializer, ConvenioSerializer
from apps.users.permissions import HasConfiguracionSistemaPermission

class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAuthenticated, HasConfiguracionSistemaPermission]

class ConvenioViewSet(viewsets.ModelViewSet):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
    permission_classes = [IsAuthenticated, HasConfiguracionSistemaPermission]
