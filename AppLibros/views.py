from django.http import HttpResponse
from django.template import Template, Context, loader
from . import models
from django.shortcuts import render


def buscar_autor(request):
    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/buscarAutor.html"
    )

    return HttpResponse(plantilla.render())


def buscar_libro(request):
    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/buscarLibro.html"
    )

    return HttpResponse(plantilla.render())


def buscar_socio(request):
    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/buscarSocio.html"
    )

    return HttpResponse(plantilla.render())


def autores(request):
    autores = models.Autor.objects.all()

    dic_autores = {"autores": autores}

    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/listadoAutores.html"
    )

    return HttpResponse(plantilla.render(dic_autores))


def libros(request):
    libros = models.Libro.objects.all()

    dic_libros = {"libros": libros}

    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/listadoLibros.html"
    )

    return HttpResponse(plantilla.render(dic_libros))


def socios(request):
    socios = models.Socio.objects.all()

    dic_socios = {"socios": socios}

    plantilla = loader.get_template(
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/listadoSocios.html"
    )

    return HttpResponse(plantilla.render(dic_socios))


def index(request):
    return render(
        request,
        "/Users/nicolasvargas/Desktop/Python/Coderhouse/Clase10Libreria/AppLibros/templates/index.html",
    )
