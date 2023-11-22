from django.contrib import admin
from .models import Prestamo

# Register your models here.


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("socio_id", "libro_id", "fecha_inicio", "fecha_fin", "devuelto")
    list_filter = ("socio_id", "libro_id")
    search_fields = ("socio_id", "libro_id")
