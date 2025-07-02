from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EjercicioViewSet, CategoriaCognitivaViewSet, SesionCognitivaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaCognitivaViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'sesiones', SesionCognitivaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]