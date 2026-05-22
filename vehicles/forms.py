from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = [
            'driver_name',
            'vehicle_type',
            'number_plate',
            'vehicle_model',
            'color',
            'phone_number',
            'nin_number',
        ]