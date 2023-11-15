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
    # URLs de CBV:
    # se requiere que la variable que se le pase al path o la ruta se llame PK, que es la representacion de Primary Key
    path("librosCBV/lista", views.LibroListView.as_view(), name="ListaLibros"),
    path("librosCBV/nuevo", views.LibroCreateView.as_view(), name="NuevoLibro"),
    path("librosCBV/<pk>", views.LibroDetailView.as_view(), name="DetalleLibro"),
    path("librosCBV/<pk>/editar", views.LibroUpdateView.as_view(), name="EditarLibro"),
    path("librosCBV/<pk>/borrar", views.LibroDeleteView.as_view(), name="BorrarLibro"),
]
