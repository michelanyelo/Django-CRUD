from django.urls import path
from . import views

app_name = "productos"
urlpatterns = [
    path("", views.index, name="ndex"),
    path("<int:producto_id>", views.detalle, name="detalle"),
]
