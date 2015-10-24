# -*- coding: utf-8 -*-

from django import forms
from anotacion.models import Anotacion


class CrearAnotacionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CrearAnotacionForm, self).__init__(*args, **kwargs)
    """
    Form de creacion de anotacion
    """
    class Meta:
        model = Anotacion
        fields = ('nombre', 'descripcion', )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de la anotacion', 'id': 'inputUserName'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Descripcion de la anotacion', 'id': 'inputUserName'}),
            #'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de Nacimiento', 'id': 'inputUserName'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
        }

class EditarAnotacionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditarAnotacionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Anotacion
        fields = (
        'nombre', 'descripcion', )

class AsignarMateriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsignarMateriaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Anotacion
        fields = (
        'materia',)