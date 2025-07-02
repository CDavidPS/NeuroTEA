from django.urls import path
from . import views
from .views import login_view, logout_view, registro_view, dashboard, ejercicio_memoria, ejercicio_atencion, ejercicio_asociaciones, ejercicio_secuencias

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),
    path('ejercicio/memoria/', ejercicio_memoria, name='ejercicio_memoria'),
    path('ejercicio/atencion/', ejercicio_atencion, name='ejercicio_atencion'),
    path('ejercicio/asociaciones/', ejercicio_asociaciones, name='ejercicio_asociaciones'),
    path('ejercicio/secuencias/', ejercicio_secuencias, name='ejercicio_secuencias'),
]
