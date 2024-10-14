from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Añadir campos personalizados al token
        token['gestion_usuarios'] = user.gestion_usuarios
        token['configuracion_sistema'] = user.configuracion_sistema
        token['generacion_reportes'] = user.generacion_reportes
        token['sistema'] = user.sistema
        return token
