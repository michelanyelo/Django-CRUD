from django.utils import timezone
from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    #personalizar el nombre de categorias en la BD
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # actualizando modelos
    # campo habilitado para actualizar automaticamente
    # para eso datetimefield(default=timezone.now)
    creado_en = models.DateTimeField(default=timezone.now)
    # cada vez que se modifica models se hace un make migration en consola
    # python manage.py makemigrations
    # luego python manage.py migrate
    
    
    #personalizar el nombre de productos en la BD
    def __str__(self):
        return self.nombre