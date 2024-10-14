from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TariffViewSet, ConvenioViewSet

router = DefaultRouter()
router.register(r'tariffs', TariffViewSet)
router.register(r'convenios', ConvenioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
