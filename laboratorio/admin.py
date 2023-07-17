from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    ordering = ['id']
    verbose_name_plural = "Laboratorios"

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ['id']
    verbose_name_plural = "Directores Generales"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')
    ordering = ['id']
    verbose_name_plural = "Productos"