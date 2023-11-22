from django.db import models

# Create your models here.


class Prestamo(models.Model):
    socio_id = models.IntegerField()
    libro_id = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    devuelto = models.BooleanField()
