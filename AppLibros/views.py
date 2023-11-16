from django.http import HttpResponse
from django.template import Template, Context, loader
from . import models
from django.shortcuts import redirect, render
from .forms import LibroForm, AutorForm, SocioForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def buscar_autor(request):
    plantilla = loader.get_template("buscarAutor.html")

    return HttpResponse(plantilla.render())


def buscar_libro(request):
    # if request.method == "GET":
    #     if request.GET["titulo"]:
    #         titulo = request.GET["titulo"]
    #         libros = models.Libro.objects.filter(titulo__icontains=titulo)
    #         return render(
    #             request, "buscarLibro.html", {"libros": libros, "tituloBuscado": titulo}
    #         )
    # else:
    #     plantilla = loader.get_template("buscarLibro.html")
    #     return HttpResponse(
    #         plantilla.render({"mensaje": "No se encontró ningun libro con ese titulo"})
    #     )
    plantilla = loader.get_template("buscarLibro.html")
    return HttpResponse(plantilla.render())


def buscar_socio(request):
    plantilla = loader.get_template("buscarSocio.html")

    return HttpResponse(plantilla.render())


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


class LibroListView(ListView):
    model = models.Libro
    context_object_name = "libros"
    template_name = "CBV_libroLista.html"


class LibroDetailView(DetailView):
    model = models.Libro
    template_name = "CBV_libroDetalle.html"


class LibroCreateView(CreateView):
    model = models.Libro
    template_name = "CBV_libroCrear.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class LibroUpdateView(UpdateView):
    model = models.Libro
    template_name = "CBV_libroEditar.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class LibroDeleteView(DeleteView):
    model = models.Libro
    template_name = "CBV_libroBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaLibros")
    fields = ["titulo", "autor", "cantidad_paginas"]


class SocioListView(ListView):
    model = models.Socio
    context_object_name = "socios"
    template_name = "CBV_socioLista.html"


class SocioDetailView(DetailView):
    model = models.Socio
    template_name = "CBV_socioDetalle.html"


class SocioCreateView(CreateView):
    model = models.Socio
    template_name = "CBV_socioCrear.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    fields = ["nombre", "apellido", "fecha_nacimiento", "ficha_id"]


class SocioUpdateView(UpdateView):
    model = models.Socio
    template_name = "CBV_socioEditar.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    fields = ["nombre", "apellido", "fecha_nacimiento", "ficha_id"]


class SocioDeleteView(DeleteView):
    model = models.Socio
    template_name = "CBV_socioBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaSocios")
    fields = ["nombre", "apellido", "fecha_nacimiento", "ficha_id"]


class AutorListView(ListView):
    model = models.Autor
    context_object_name = "autores"
    template_name = "CBV_autorLista.html"


class AutorDetailView(DetailView):
    model = models.Autor
    template_name = "CBV_autorDetalle.html"


class AutorCreateView(CreateView):
    model = models.Autor
    template_name = "CBV_autorCrear.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    fields = ["nombre", "apellido", "fecha_nacimiento"]


class AutorUpdateView(UpdateView):
    model = models.Autor
    template_name = "CBV_autorEditar.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    fields = ["nombre", "apellido", "fecha_nacimiento"]


class AutorDeleteView(DeleteView):
    model = models.Autor
    template_name = "CBV_autorBorrar.html"
    success_url = reverse_lazy("AppLibros:ListaAutores")
    fields = ["nombre", "apellido", "fecha_nacimiento"]
