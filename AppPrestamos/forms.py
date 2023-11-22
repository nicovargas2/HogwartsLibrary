from django import forms
from .models import Prestamo


class DateInput(forms.DateInput):
    input_type = "date"


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ["socio_id", "libro_id", "fecha_inicio", "fecha_fin", "devuelto"]
        widgets = {
            "fecha_inicio": DateInput(),
            "fecha_fin": DateInput(),
        }
