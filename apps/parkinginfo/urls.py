from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingInfoViewSet

router = DefaultRouter()
router.register(r'parkinginfo', ParkingInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
