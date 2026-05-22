from django.urls import path
from .views import vehicle_register, vehicle_list, vehicle_detail

urlpatterns = [
    path('', vehicle_list, name='vehicle_list'),
    path('vehicles/register/', vehicle_register, name='vehicle_register'),
    path('vehicles/<int:pk>/', vehicle_detail, name='vehicle_detail'),
]