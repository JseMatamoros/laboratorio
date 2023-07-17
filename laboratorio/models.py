from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default="Sin especialidad")

    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    director_general = models.ForeignKey(DirectorGeneral, on_delete=models.CASCADE, null=True, blank=True)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
