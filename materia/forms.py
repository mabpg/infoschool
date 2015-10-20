# -*- coding: utf-8 -*-

from django import forms

from materia.models import Materia, Materia_curso



class CrearMateriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CrearMateriaForm, self).__init__(*args, **kwargs)
    """
    Form de creacion de materia
    """
    class Meta:
        model = Materia
        fields = ('nombre', )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de la materia', 'id': 'inputUserName'}),
            #'profesor': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Profesor', 'id': 'inputUserName'}),
        }
        labels = {
            'nombre_usuario': 'Nombre',
            #'profesor': 'Profesor',
        }

class EditarMateriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditarMateriaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Materia
        fields = (
        'nombre', )

class AsignarMateriaCursoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsignarMateriaCursoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Materia_curso
        fields = (
        'curso', 'materia')