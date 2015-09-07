# -*- coding: utf-8 -*-
from django import forms

class AutenticarForm(forms.Form):
    """
    El formulario AutenticarForm creado para realizar la autenticación con la vista ingresar.
    @param username: Aquí se almacena el nombre de usuario al utilizarlo en la vista, el mismo en de tipo charfield con atributos customizados para CSS.
    @param password: Aquí se almacena la contraseña al utilizarlo en la vista, el mismo en de tipo charfield con atributos customizados para CSS.
    """
    username = forms.CharField(max_length=50,
                               label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password', 'id': 'inputUserName'}))

class RecuperarForm(forms.Form):
    """
    El formulario RecuperarForm creado para realizar la recuperación con la vista ingresar.
    @param nombre_de_usuario: Aquí se almacena el nombre de usuario al utilizarlo en la vista, el mismo en de tipo charfield con atributos customizados para CSS.
    """
    nombre_de_usuario = forms.CharField(max_length=50,
                                        label='',
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nombre de Usuario', 'id': 'inputUserName'}))



