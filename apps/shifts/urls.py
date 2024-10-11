from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShiftViewSet, VehicleCountsInShiftView

router = DefaultRouter()
router.register(r'shifts', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shifts/<int:pk>/close/', ShiftViewSet.as_view({'post': 'close_shift'}), name='close-shift'),
    path('vehicle-counts/', VehicleCountsInShiftView.as_view(), name='vehicle-counts-in-shift'),
]
