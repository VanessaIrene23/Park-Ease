from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    ROLES_CHOICES =[
        ("system admin","System Admin"),
        ("manager", "Manager"),
        ("park attendant","Park Attendant")
    ]
    role = forms.ChoiceField(choices=ROLES_CHOICES)
    class Meta:
        model = User
        fields = [
            "username","email","password1","password2"
        ]