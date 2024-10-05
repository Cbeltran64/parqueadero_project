from django.urls import path
from apps.vehicles.views import VehicleCountsView

urlpatterns = [
    path('vehicle-counts/', VehicleCountsView.as_view(), name='vehicle-counts'),
]
