from django.urls import path
from . import views

urlpatterns = [
    path("buscarLibro/", views.buscar_libro, name="buscar_libro"),
    path("libros/", views.libros, name="libros"),
    path("buscarAutor/", views.buscar_autor, name="buscar_autor"),
    path("autores/", views.autores, name="autores"),
    path("buscarSocio/", views.buscar_socio, name="buscar_socio"),
    path("socios/", views.socios, name="socios"),
    path("index/", views.index, name="index"),
]
