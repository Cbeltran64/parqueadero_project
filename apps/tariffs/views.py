from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Tariff, Convenio
from .serializers import TariffSerializer, ConvenioSerializer
from rest_framework.permissions import IsAdminUser

class TariffViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Verificar si existen registros asociados antes de eliminar
        if instance.tarifas.exists():
            return Response({"error": "No se puede eliminar la tarifa ya que tiene convenios asociados."}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConvenioViewSet(viewsets.ModelViewSet):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
    permission_classes = [IsAuthenticated]
