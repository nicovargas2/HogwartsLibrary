from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=80)
    autor = models.CharField(max_length=120)
    cantidad_paginas = models.IntegerField()

    def __str__(self) -> str:
        return f"titulo: {self.titulo} - autor: {self.autor} - cantidad de paginas: {self.cantidad_paginas}"


class Autor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - fecha de nacimiento: {self.fecha_nacimiento}"


class Socio(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    # ficha_id = models.IntegerField()
    email = models.EmailField(default="a@a.com")

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - fecha de nacimiento: {self.fecha_nacimiento} - ficha: {self.ficha_id}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
