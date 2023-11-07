from django.db import models

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=80)
    autor = models.CharField(max_length=120)
    cantidad_paginas = models.IntegerField()


class Autor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()


class Socio(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    ficha_id = models.IntegerField()
