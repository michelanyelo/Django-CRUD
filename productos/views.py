from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ProductoForm
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


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(
        request, 
        "detalle.html", 
        context={"producto": producto}
    )


def formulario(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos")
    else:
        form = ProductoForm()
        
    return render(
        request, 
        "producto_form.html", 
        {"form": form}
    )
