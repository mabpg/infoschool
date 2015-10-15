# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms

from alumno import models
from alumno.models import Alumno



#class UserForm(forms.ModelForm):
#    class Meta:
#        model = Alumno
#        fields = ('username', 'first_name', 'last_name', 'email')


class CrearAlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CrearAlumnoForm, self).__init__(*args, **kwargs)
    """
    Form de creacion de alumno
    """
    class Meta:
        model = Alumno
        fields = ('fecha_nacimiento', )
        widgets = {
            #'usuario': forms.TextInput(attrs={'class': 'form-control', 'type': User, 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de Nacimiento', 'id': 'inputUserName'}),
        }
        labels = {
            #'usuario': 'Nombre',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }

class EditarAlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditarAlumnoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Alumno
        fields = (
        'fecha_nacimiento',)
        widgets = {
            #'usuario': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Fecha Nacimiento', 'id': 'inputUserName'}),

        }
        labels = {
            'usuario': 'Nombre',
            'fecha_nacimiento': 'Fecha de Nacimiento',

        }