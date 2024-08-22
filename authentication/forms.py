from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=None  # Eliminar el texto de ayuda
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=None  # Eliminar el texto de ayuda
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': None,  # Eliminar el texto de ayuda predeterminado
            'password1': None,
            'password2': None,
        }
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }