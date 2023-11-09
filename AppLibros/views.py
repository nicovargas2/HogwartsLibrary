from django.http import HttpResponse
from django.template import Template, Context, loader
from . import models
from django.shortcuts import redirect, render
from .forms import LibroForm, AutorForm, SocioForm


def buscar_autor(request):
    plantilla = loader.get_template("buscarAutor.html")

    return HttpResponse(plantilla.render())


def buscar_libro(request):
    plantilla = loader.get_template("buscarLibro.html")

    return HttpResponse(plantilla.render())


def buscar_socio(request):
    plantilla = loader.get_template("buscarSocio.html")

    return HttpResponse(plantilla.render())


def listar_autores(request):
    autores = models.Autor.objects.all()

    dic_autores = {"autores": autores}

    plantilla = loader.get_template("listadoAutores.html")

    return HttpResponse(plantilla.render(dic_autores))


def listar_libros(request):
    libros = models.Libro.objects.all()

    dic_libros = {"libros": libros}

    plantilla = loader.get_template("listadoLibros.html")

    return HttpResponse(plantilla.render(dic_libros))


def listar_socios(request):
    socios = models.Socio.objects.all()

    dic_socios = {"socios": socios}

    plantilla = loader.get_template("listadoSocios.html")

    return HttpResponse(plantilla.render(dic_socios))


def index(request):
    return render(request, "index.html")


def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect("AppLibros:index")
    else:
        form = LibroForm()

    return render(request, "libro_form.html", {"form": form})


def agregar_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            return redirect("AppLibros:index")
    else:
        form = SocioForm()

    return render(request, "socio_form.html", {"form": form})


def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect("AppLibros:index")
    else:
        form = AutorForm()

    return render(request, "autor_form.html", {"form": form})
