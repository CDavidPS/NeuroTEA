from django.db import models
from usuarios.models import Usuario

class CategoriaCognitiva(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaCognitiva, on_delete=models.CASCADE)
    nivel_dificultad = models.IntegerField()  # 1 = fácil, 5 = difícil
    contenido = models.JSONField()  # Aquí va el contenido interactivo (ej: imágenes, preguntas, audio)

    def __str__(self):
        return f"{self.titulo} (Nivel {self.nivel_dificultad})"
    
class SesionCognitiva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    tiempo_dedicado = models.IntegerField(help_text="Tiempo en segundos")
    nivel_logrado = models.IntegerField(default=1)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.ejercicio.titulo} - {self.fecha.date()}"