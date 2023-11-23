from django import forms
from .models import Libro, Autor, Socio
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "cantidad_paginas"]


class DateInput(forms.DateInput):
    input_type = "date"


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellido", "fecha_nacimiento"]
        widgets = {
            "fecha_nacimiento": DateInput(),
        }


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ["nombre", "apellido", "fecha_nacimiento", "email"]
        widgets = {
            "fecha_nacimiento": DateInput(),
        }


class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario", min_length=5, max_length=15)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"]
        # Para sacar los mensajes de ayuda
        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email: ")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]
