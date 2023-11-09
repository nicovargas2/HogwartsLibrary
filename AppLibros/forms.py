from django import forms
from .models import Libro, Autor, Socio


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "cantidad_paginas"]


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellido", "fecha_nacimiento"]


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ["nombre", "apellido", "fecha_nacimiento", "ficha_id"]
