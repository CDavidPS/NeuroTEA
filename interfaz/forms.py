from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuarios.models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
