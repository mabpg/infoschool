# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms

from usuario import models
from usuario.models import Usuario



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CrearUsuarioForm(forms.ModelForm):
    """
    Form de creacion de usuario
    """
    class Meta:
        model = models.Usuario
        fields = ['nombre_usuario', 'password', 'nombre', 'apellido', 'correo_electronico']
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password', 'id': 'inputUserName'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre', 'id': 'inputUserName'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Apellido', 'id': 'inputUserName'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Correo Electronico', 'id': 'inputUserName'}),
        }
        labels = {
            'nombre_usuario': '',
            'password': '',
            'nombre': '',
            'apellido': '',
            'correo_electronico': '',
        }

class EditarUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditarUsuarioForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = (
        'nombre', 'apellido', 'correo_electronico', 'cedula', 'telefono', 'direccion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Apellido', 'id': 'inputUserName'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Correo Electronico', 'id': 'inputUserName'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Cedula', 'id': 'inputUserName'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Telefono', 'id': 'inputUserName'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Direccion', 'id': 'inputUserName'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo_electronico': 'Correo Electronico',
            'cedula': 'Cedula',
            'telefono': 'Telefono',
            'Direccion': 'Direccion',
        }



