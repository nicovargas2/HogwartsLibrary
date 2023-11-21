from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "AppLibros"


urlpatterns = [
    path("index/", views.index, name="index"),
    path("libro/buscar", views.buscar_libro, name="buscar_libro"),
    path("libro/buscar/resultados", views.buscar_libro_accion),
    path("autor/buscar", views.buscar_autor, name="buscar_autor"),
    path("autor/buscar/resultados", views.buscar_autor_accion),
    path("socio/buscar", views.buscar_socio, name="buscar_socio"),
    path("socio/buscar/resultados", views.buscar_socio_accion),
    # path("libro/agregar/", views.agregar_libro, name="agregar_libro"),
    # path("libros/", views.listar_libros, name="libros"),
    # path("autor/agregar/", views.agregar_autor, name="agregar_autor"),
    # path("autores/", views.listar_autores, name="autores"),
    # path("socio/agregar", views.agregar_socio, name="agregar_socio"),
    # path("socios/", views.listar_socios, name="socios"),
    # URLs de CBV:
    # se requiere que la variable que se le pase al path o la ruta se llame PK, que es la representacion de Primary Key
    path("libros/lista", views.LibroListView.as_view(), name="ListaLibros"),
    path("libros/nuevo", views.LibroCreateView.as_view(), name="NuevoLibro"),
    path("libros/<pk>", views.LibroDetailView.as_view(), name="DetalleLibro"),
    path("libros/<pk>/editar", views.LibroUpdateView.as_view(), name="EditarLibro"),
    path("libros/<pk>/borrar", views.LibroDeleteView.as_view(), name="BorrarLibro"),
    path("socios/lista", views.SocioListView.as_view(), name="ListaSocios"),
    path("socios/nuevo", views.SocioCreateView.as_view(), name="NuevoSocio"),
    path("socios/<pk>", views.SocioDetailView.as_view(), name="DetalleSocio"),
    path("socios/<pk>/editar", views.SocioUpdateView.as_view(), name="EditarSocio"),
    path("socios/<pk>/borrar", views.SocioDeleteView.as_view(), name="BorrarSocio"),
    path("autores/lista", views.AutorListView.as_view(), name="ListaAutores"),
    path("autores/nuevo", views.AutorCreateView.as_view(), name="NuevoAutor"),
    path("autores/<pk>", views.AutorDetailView.as_view(), name="DetalleAutor"),
    path("autores/<pk>/editar", views.AutorUpdateView.as_view(), name="EditarAutor"),
    path("autores/<pk>/borrar", views.AutorDeleteView.as_view(), name="BorrarAutor"),
    # Login
    path("login", views.login_request, name="Login"),
    path("registro", views.registro, name="Registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
]
