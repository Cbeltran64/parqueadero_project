from django.urls import path, include
from .views import CustomTokenObtainPairView, LogoutView, UserMenuPermissionsView
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet
from django.contrib import admin
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/users/menu-permissions/', UserMenuPermissionsView.as_view(), name='user_menu_permissions'),
    path('api/', include(router.urls)),
    path('api/', include('apps.parkinginfo.urls')),
    path('api/', include('apps.tariffs.urls')),
]