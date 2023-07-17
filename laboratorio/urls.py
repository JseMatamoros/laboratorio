from django.urls import path
# from .views import index
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('laboratorios/', views.mostrar_laboratorios, name='mostrar_laboratorios'),
    path('laboratorios/insertar/', views.insertar_laboratorio, name='insertar_laboratorio'),
    path('laboratorios/<int:id>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('laboratorios/<int:id>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]


