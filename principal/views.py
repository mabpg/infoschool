# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

from django.shortcuts import render_to_response, RequestContext, render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from principal.forms import RecuperarForm, AutenticarForm
from usuario.models import Usuario
from materia.models import Materia

def ingresar(request):
    """
    La vista 'ingresar' realiza las siguientes acciones:
    1) En caso de que el método del request sea un POST:
        Intenta autenticar al usuario y remitirlo al home. En casos contrarios lo remite a donde corresponde.
    2) Si el método es un GET:
        Renderiza el template y remite el formulario correspondiente.

    @param formulario: Formulario de tipo AutenticarForm
    @type AutenticarForm: Formulario con nombre y password para autenticaciones.
    @return: 1) Si es un POST:
                Retorna A: Redirección a /home si la autenticación es correcta y se encuentra activo.
                Retorna B: Renderiza a noactivo.html si la autenticación es correcta y se encuentra inactivo.
                Retorna C: Renderiza a nousuario.html si el usuario no existe.
             2) Si es un GET:
                Renderiza ingresar.html
    """
    if request.method == 'POST':
        formulario = AutenticarForm(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/home')
                    #return HttpResponseRedirect('/usuario')
                else:
                    return render_to_response('autenticacion/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('autenticacion/nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AutenticarForm()
    return render_to_response('autenticacion/ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def recuperar_contrasenha(request):
    """
    Recuperar contraseña
    @param request: http request
    Funcion que se encarga de la remision de un correo de recuperación
    """
    #if not request.user.is_anonymous():
    #    return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = RecuperarForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['nombre_de_usuario']
            us = Usuario.objects.filter(nombre_usuario = usuario)
            if us.__len__() != 0:
                if us[0].is_active:
                    #creamos un password aleatorio y lo guardamos
                    new_pass = Usuario.objects.make_random_password(length=15)
                    us[0].set_password(new_pass)
                    us[0].save()
                    #enviamos el nuevo password al correo del usuario

                    # Creamos el mensaje
                    msg = MIMEText(new_pass)

                    # Conexion con el server

                    msg['Subject'] = new_pass
                    msg['From'] = 'scrumbanpy@gmail.com'
                    msg['To'] = us[0].correo_electronico

                    # Autenticamos
                    mailServer = smtplib.SMTP('smtp.gmail.com',587)
                    mailServer.ehlo()
                    mailServer.starttls()
                    mailServer.ehlo()
                    mailServer.login("scrumbanpy@gmail.com","mipassword")

                    # Enviamos
                    mailServer.sendmail("scrumbanpy@gmail.com", us[0].correo_electronico, msg.as_string())

                    # Cerramos conexion
                    mailServer.close()

                    return render_to_response('autenticacion/password_enviado.html')
                else:
                    return render_to_response('autenticacion/noactivo.html')
            else:
                return render_to_response('autenticacion/noexiste.html')
    else:
        formulario = RecuperarForm()
    return render_to_response('autenticacion/recuperar_contrasenha.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required
def home_sistema(request):
    """
    Home page Por ahora solo contiene una lista de los modulos disponibles
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    data={}
    usuario_actual = request.user
    data['admin'] = False
    data['alum'] = False
    data['profe'] = False
    if(usuario_actual.is_admin==True):
        data['admin'] = True

    if(usuario_actual.clase=='Profesor'):
        data['profe']=True

    if(usuario_actual.clase=='Alumno'):
        data['alum']=True

    template_name = 'home.html'
    return render(request, template_name, data)



