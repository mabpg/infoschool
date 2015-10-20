# -*- coding: utf-8 -*-

from django import forms

from curso.models import Curso



class CrearCursoForm(forms.ModelForm):
    """
    Form de creacion de curso
    """
    def __init__(self, *args, **kwargs):
        super(CrearCursoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Curso
        fields = ['nombre', 'seccion', 'turno', 'especialidad']


class EditarCursoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditarCursoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Curso
        fields = (
        'nombre', 'seccion', 'turno', 'especialidad')