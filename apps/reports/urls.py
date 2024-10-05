from django.urls import path
from .views import ReportView

urlpatterns = [
    path('reports/<str:period>/', ReportView.as_view(), name='reports'),
]
