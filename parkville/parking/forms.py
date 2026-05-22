from django import forms
from .models import ParkingSession
import re

class SignOutForm(forms.ModelForm):
    class Meta:
        model = ParkingSession
        fields = ['receiver_name', 'receiver_phone', 'receiver_gender', 'receiver_nin']
        widgets = {
            'receiver_gender': forms.Select(choices=[('', 'Select Gender'), ('male', 'Male'), ('female', 'Female')]),
        }

    def clean_receiver_name(self):
        name = self.cleaned_data.get('receiver_name')
        if not name[0].isupper():
            raise forms.ValidationError("Name must start with a capital letter.")
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name must not contain numbers.")
        return name

    def clean_receiver_phone(self):
        phone = self.cleaned_data.get('receiver_phone')
        pattern = r'^(07|06)\d{8}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError("Enter a valid Ugandan phone number e.g 0701234567.")
        return phone