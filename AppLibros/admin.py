from django.contrib import admin
from .models import Autor
from .models import Libro
from .models import Socio


# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha_nacimiento")
    list_filter = ("nombre", "apellido")
    search_fields = ("nombre", "apellido")


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "cantidad_paginas")
    list_filter = ("titulo", "autor")
    search_fields = ("titulo", "autor")


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("ficha_id", "nombre", "apellido", "fecha_nacimiento")
    list_filter = ("nombre", "apellido")
    search_fields = ("nombre", "apellido")