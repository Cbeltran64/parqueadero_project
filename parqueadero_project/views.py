from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import viewsets
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer, UserCreateSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Vista para el token de acceso personalizado
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Vista del CRUD para los usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        serializer.save()


# Vista para cerrar sesión (blacklisting de tokens)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = OutstandingToken.objects.get(token=request.auth)
            BlacklistedToken.objects.create(token=token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Vista para obtener los permisos de menú del usuario autenticado
class UserMenuPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        permissions = {
            "gestion_usuarios": user.gestion_usuarios,
            "configuracion_sistema": user.configuracion_sistema,
            "generacion_reportes": user.generacion_reportes,
            "sistema": user.sistema,
        }
        return Response(permissions)
