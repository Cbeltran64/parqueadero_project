from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MenuOption
from apps.users.permissions import IsAdmin

class MenuView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == 'admin':
            menu = MenuOption.objects.all()
        else:
            menu = user.menu_permissions.all()
        menu_data = [{"id": item.id, "name": item.name} for item in menu]
        return Response(menu_data)
