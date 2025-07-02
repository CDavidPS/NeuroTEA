from rest_framework import viewsets
from .models import Ejercicio, CategoriaCognitiva, SesionCognitiva
from .serializers import EjercicioSerializer, CategoriaCognitivaSerializer, SesionCognitivaSerializer

class CategoriaCognitivaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaCognitiva.objects.all()
    serializer_class = CategoriaCognitivaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class SesionCognitivaViewSet(viewsets.ModelViewSet):
    queryset = SesionCognitiva.objects.all()
    serializer_class = SesionCognitivaSerializer