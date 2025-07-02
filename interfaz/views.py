from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
# Create your views here.

def inicio(request):
    return render(request, 'interfaz/index.html')

@login_required
def dashboard(request):
    if request.user.rol == 'terapeuta':
        template = 'interfaz/dashboard_terapeuta.html'
    elif request.user.rol == 'cuidador':
        template = 'interfaz/dashboard_cuidador.html'
    else:
        template = 'interfaz/dashboard.html'
    return render(request, template)

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'interfaz/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'interfaz/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def ejercicio_memoria(request):
    return render(request, 'interfaz/ejercicio_memoria.html')

def ejercicio_atencion(request):
    numeros = range(1, 17)
    return render(request, 'interfaz/ejercicio_atencion.html', {'numeros': numeros})

def ejercicio_asociaciones(request):
    return render(request, 'interfaz/ejercicio_asociaciones.html')

def ejercicio_secuencias(request):
    return render(request, 'interfaz/ejercicio_secuencias.html')

