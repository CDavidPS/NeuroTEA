from rest_framework import serializers
from .models import Ejercicio, CategoriaCognitiva, SesionCognitiva

class CategoriaCognitivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaCognitiva
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'  

class SesionCognitivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionCognitiva
        fields = '__all__'