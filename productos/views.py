from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.


# /productos
def index(request):
    # listar elementos
    # ir a buscar los datos
    # todos los registros con el siguiente metodo
    productos = Producto.objects.all().values()
    # # argumentos nombrados
    # # puntaje__lte (menor igual que) puntaje__gte(mayor igual que)
    # productos = Producto.objects.filter(puntaje=3)
    # # buscar un elemento en particular
    # productos = Producto.objects.get(id=1)
    # print(productos)

    # usar jsonresponse para mostrar la lista de datos como json
    return JsonResponse(list(productos), safe=False)
