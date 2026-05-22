from django.urls import path
from .views import sign_out, receipt

urlpatterns = [
    path('vehicles/signout/<int:pk>/', sign_out, name='sign_out'),
    path('receipt/<int:pk>/', receipt, name='receipt'),
]