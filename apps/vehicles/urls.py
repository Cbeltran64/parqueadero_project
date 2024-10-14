from django.urls import path
from apps.vehicles.views import VehicleViewSet

urlpatterns = [
    path('vehicle-counts/', VehicleViewSet.as_view(), name='vehicle-counts'),
]
