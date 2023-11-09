from django.urls import path
from . import views

app_name = "AppLibros"


urlpatterns = [
    path("libro/buscar", views.buscar_libro, name="buscar_libro"),
    path("libro/agregar/", views.agregar_libro, name="agregar_libro"),
    path("libros/", views.listar_libros, name="libros"),
    path("autor/buscar", views.buscar_autor, name="buscar_autor"),
    path("autor/agregar/", views.agregar_autor, name="agregar_autor"),
    path("autores/", views.listar_autores, name="autores"),
    path("socio/buscar", views.buscar_socio, name="buscar_socio"),
    path("socio/agregar", views.agregar_socio, name="agregar_socio"),
    path("socios/", views.listar_socios, name="socios"),
    path("index/", views.index, name="index"),
]
