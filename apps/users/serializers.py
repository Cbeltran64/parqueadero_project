from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'is_staff', 'is_active',
            'gestion_usuarios', 'configuracion_sistema', 'generacion_reportes', 'sistema'
        ]

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            if password:
                instance.set_password(password)
            return super().update(instance, validated_data)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'email', 'is_staff', 'is_active',
            'gestion_usuarios', 'configuracion_sistema', 'generacion_reportes', 'sistema'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
