from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import PrestamoForm
from django.contrib import messages
from AppLibros.models import Socio, Libro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


@login_required
def index(request):
    if request.method == "GET":
        # messages.info(request, "Ingrese al menos 3 letras en su busqueda")
        lista_nombres = buscar_socios()
        lista_libros = buscar_libros()
        form = PrestamoForm()
        return render(
            request,
            "indexPrest.html",
            {
                "form": form,
                "lista_nombres": lista_nombres,
                "lista_libros": lista_libros,
            },
        )

    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success = (request, f"Prestamo registrado!")
            return redirect("AppPrestamos:index")

    form = PrestamoForm()
    return render(request, "indexPrest.html", {"form": form})


def buscar_socios():
    lista_socios = Socio.objects.all()
    return lista_socios


def buscar_libros():
    lista_libros = Libro.objects.all()
    return lista_libros


class PrestamoListView(LoginRequiredMixin, ListView):
    model = models.Prestamo
    context_object_name = "prestamos"
    template_name = "CBV_prestamoLista.html"


class PrestamoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Prestamo
    template_name = "CBV_prestamoEditar.html"
    success_url = reverse_lazy("AppPrestamos:index")
    fields = ["socio_id", "libro_id", "fecha_inicio", "fecha_fin", "devuelto"]
