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
    usuario_actual = request.user
    """roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    usuarios = {}
    for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
        creacion = permisos_asociados.crear_usuario
        modificacion = permisos_asociados.modificar_usuario
        eliminacion = permisos_asociados.eliminar_usuario
        #usuarios['crear_usuario']= creacion
        #usuarios['modificar_usuario']= modificacion
        #usuarios['eliminar_usuario']= eliminacion
        if creacion==True or modificacion== True or eliminacion==True:
            usuarios['usuarios'] = True
        else:
            usuarios['usuarios'] = False

        creacion = permisos_asociados.crear_rol
        modificacion = permisos_asociados.modificar_rol
        eliminacion = permisos_asociados.eliminar_rol
        if creacion==True or modificacion== True or eliminacion==True:
            usuarios['roles'] = True
        else:
            usuarios['roles'] = False

        creacion = permisos_asociados.crear_flujo
        modificacion = permisos_asociados.modificar_flujo
        eliminacion = permisos_asociados.eliminar_flujo
        if creacion==True or modificacion== True or eliminacion==True:
            usuarios['flujos'] = True
        else:
            usuarios['flujos'] = False

        creacion = permisos_asociados.crear_proyecto
        modificacion = permisos_asociados.modificar_proyecto
        eliminacion = permisos_asociados.eliminar_proyecto
        cancelacion = permisos_asociados.cancelar_proyecto
        if creacion==True or modificacion== True or eliminacion==True or cancelacion==True:
            usuarios['proyectos'] = True
        else:
            usuarios['proyectos'] = False"""

    """
    #PROYECTO
    roles_proyecto_usuario = list(Usuario_Rol_Proyecto.objects.filter(usuario=usuario_actual)) #traemos todos los roles de proyecto que se han asignado al usuario en cuestion

    #lista de proyectos del usuario
    lista_proyectos=[]
    creacion=None
    modificacion=None

    for i in roles_proyecto_usuario:
        lista_proyectos.append(i.proyecto)

    for i in roles_proyecto_usuario:
        permisos_asociados = i.roles.permiso_proyecto
        creacion = permisos_asociados.crear_flujo or permisos_asociados.crear_sprint or permisos_asociados.crear_user_story or permisos_asociados.crear_release or permisos_asociados.crear_rol
        modificacion = permisos_asociados.modificar_flujo or permisos_asociados.modificar_sprint or permisos_asociados.modificar_user_story or permisos_asociados.modificar_rol
    """
    data={}
    #data['permiso_ingresar']=creacion or modificacion
    #data['mostrar']=usuarios

    #lista_proyectos=Materia.objects.all()
    #data['lista_proyectos']=lista_proyectos
    template_name = 'home.html'
    return render(request, template_name, data)



