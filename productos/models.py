from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
