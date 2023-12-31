from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.


# /productos
def index(request):
    productos = Producto.objects.all()
    return render(
        # primer argumento objeto request
        request,
        # string donde se ubica la plantilla y nombre
        "index.html",
        # datos del renderizado
        context={"productos": productos},
    )
