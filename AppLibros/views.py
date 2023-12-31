from django.http import HttpResponse
from django.template import Template, Context, loader
from . import models
from django.shortcuts import redirect, render
from .forms import LibroForm, AutorForm, SocioForm, UserCreationFormCustom, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User


@login_required
def buscar_autor(request):
    plantilla = loader.get_template("buscarAutor.html")
    return HttpResponse(plantilla.render())


@login_required
def buscar_autor_accion(request):
    if request.method == "GET":
        autor_buscado = request.GET["autorBuscado"]
        autores = models.Autor.objects.filter(nombre__icontains=autor_buscado)
        return render(
            request,
            "buscarAutor.html",
            {"autores": autores, "autor_buscado": autor_buscado},
        )
    else:
        mensaje = "No se encontró ningun autor"
        plantilla = loader.get_template("buscarAutor.html")
        return HttpResponse(plantilla.render({"mensaje": mensaje}))


@login_required
def buscar_libro(request):
    plantilla = loader.get_template("buscarLibro.html")
    return HttpResponse(plantilla.render())


@login_required
def buscar_libro_accion(request):
    if request.method == "GET":
        titulo_buscado = request.GET["tituloBuscado"]
        libros = models.Libro.objects.filter(titulo__icontains=titulo_buscado)
        return render(
            request,
            "buscarLibro.html",
            {"libros": libros, "titulo_buscado": titulo_buscado},
        )
    else:
        mensaje = "No se encontró ningun libro con ese titulo"
        plantilla = loader.get_template("buscarLibro.html")
        return HttpResponse(plantilla.render({"mensaje": mensaje}))


@login_required
def buscar_socio(request):
    plantilla = loader.get_template("buscarSocio.html")
    return HttpResponse(plantilla.render())


@login_required
def buscar_socio_accion(request):
    if request.method == "GET":
        socio_buscado = request.GET["socioBuscado"]
        socios = models.Socio.objects.filter(nombre__icontains=socio_buscado)
        return render(
            request,
            "buscarSocio.html",
            {"socios": socios, "socio_buscado": socio_buscado},
        )
    else:
        mensaje = "No se encontró ningun socio con ese nombre"
        plantilla = loader.get_template("buscarSocio.html")
        return HttpResponse(plantilla.render({"mensaje": mensaje}))


# def listar_autores(request):
#     autores = models.Autor.objects.all()
#     dic_autores = {"autores": autores}
#     plantilla = loader.get_template("listadoAutores.html")
#     return HttpResponse(plantilla.render(dic_autores))


# def listar_libros(request):
#     libros = models.Libro.objects.all()
#     dic_libros = {"libros": libros}
#     plantilla = loader.get_template("listadoLibros.html")
#     return HttpResponse(plantilla.render(dic_libros))


# def listar_socios(request):
#     socios = models.Socio.objects.all()
#     dic_socios = {"socios": socios}
#     plantilla = loader.get_template("listadoSocios.html")
#     return HttpResponse(plantilla.render(dic_socios))


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# def agregar_libro(request):
#     if request.method == "POST":
#         form = LibroForm(request.POST)
#         if form.is_valid():
#             libro = form.save()
#             return redirect("AppLibros:index")
#     else:
#         form = LibroForm()
#     return render(request, "libro_form.html", {"form": form})


# def agregar_socio(request):
#     if request.method == "POST":
#         form = SocioForm(request.POST)
#         if form.is_valid():
#             socio = form.save()
#             return redirect("AppLibros:index")
#     else:
#         form = SocioForm()
#     return render(request, "socio_form.html", {"form": form})


# def agregar_autor(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST)
#         if form.is_valid():
#             autor = form.save()
#             return redirect("AppLibros:index")
#     else:
#         form = AutorForm()
#     return render(request, "autor_form.html", {"form": form})


class LibroListView(LoginRequiredMixin, ListView):
    model = models.Libro
    context_object_name = "libros"
    template_name = "CBV_libroLista.html"


class LibroDetailView(LoginRequiredMixin, DetailView):
    model = models.Libro
    template_name = "CBV_libroDetalle.html"


class LibroCreateView(LoginRequiredMixin, CreateView):
    model = models.Libro
    template_name = "CBV_libroCrear.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Libro
    template_name = "CBV_libroEditar.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Libro
    template_name = "CBV_libroBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class SocioListView(LoginRequiredMixin, ListView):
    model = models.Socio
    context_object_name = "socios"
    template_name = "CBV_socioLista.html"


class SocioDetailView(LoginRequiredMixin, DetailView):
    model = models.Socio
    template_name = "CBV_socioDetalle.html"


class SocioCreateView(LoginRequiredMixin, CreateView):
    model = models.Socio
    form_class = SocioForm
    template_name = "CBV_socioCrear.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    # fields = ["nombre", "apellido", "fecha_nacimiento", "ficha_id"]


class SocioUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Socio
    template_name = "CBV_socioEditar.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    fields = ["nombre", "apellido", "fecha_nacimiento", "email"]


class SocioDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Socio
    template_name = "CBV_socioBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    fields = ["nombre", "apellido", "fecha_nacimiento", "email"]


class AutorListView(LoginRequiredMixin, ListView):
    model = models.Autor
    context_object_name = "autores"
    template_name = "CBV_autorLista.html"


class AutorDetailView(LoginRequiredMixin, DetailView):
    model = models.Autor
    template_name = "CBV_autorDetalle.html"


class AutorCreateView(LoginRequiredMixin, CreateView):
    model = models.Autor
    form_class = AutorForm
    template_name = "CBV_autorCrear.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    # fields = ["nombre", "apellido", "fecha_nacimiento"]


class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Autor
    template_name = "CBV_autorEditar.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    fields = ["nombre", "apellido", "fecha_nacimiento"]


class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Autor
    template_name = "CBV_autorBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    fields = ["nombre", "apellido", "fecha_nacimiento"]


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasena)

            login(request, user)
            return render(request, "index.html")
        else:
            return render(
                request, "index.html", {"mensaje": f"Usuario o contraseña incorrectos."}
            )
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def registro(request):
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            form.save()
            new_user_username = form.cleaned_data.get("username")
            messages.success = (request, f"Usuario {new_user_username}creado")
            form = UserCreationFormCustom()
    else:
        form = UserCreationFormCustom()

    context = {"form": form}
    return render(request, "registro.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect("AppLibros:index")


def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "index.html")
    else:
        miFormulario = UserEditForm(instance=request.user)
    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})


class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiarPass.html"
    success_url = reverse_lazy("AppLibros:EditarPerfil")
