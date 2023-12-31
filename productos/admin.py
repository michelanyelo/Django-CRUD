from django.contrib import admin
# importar modelos para visualizarlos en internet
from .models import Categoria, Producto
# Register your models here.

# con lo anterior añadir estas instrucciones
admin.site.register(Categoria)
admin.site.register(Producto)

