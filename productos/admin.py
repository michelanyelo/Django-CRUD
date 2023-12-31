from django.contrib import admin

# importar modelos para visualizarlos en internet
from .models import Categoria, Producto

# Register your models here.

# con lo anterior añadir estas instrucciones
# y como segundo metodo van las personalizaciones
# que se ven en la base de datos del navegador


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


class ProductoAdmin(admin.ModelAdmin):
    exclude = ("creado_en", )
    list_display = ("id", "nombre", "stock", "categoria", "creado_en")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
