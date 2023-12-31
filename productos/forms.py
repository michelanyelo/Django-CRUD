from . import models
from django.forms import ModelForm


class ProductoForm(ModelForm):
    # esta clase va siempre
    class Meta:
        model = models.Producto
        fields = ["nombre", "stock", "puntaje", "categoria"]
