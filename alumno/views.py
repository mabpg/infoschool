# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from usuario.forms import CrearUsuarioForm, EditarUsuarioForm
from usuario.models import Usuario
from alumno.models import Alumno


@login_required
def listar_alumnos(request, template_name='alumno/listar_alumno.html'):
    """
    Lista de alumnos
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    data = {}
    """if roles_sistema_usuarios.__len__()>0:
        for i in roles_sistema_usuarios:
            permisos_asociados = i.roles.permiso_sistema
            creacion = permisos_asociados.crear_usuario
            modificacion = permisos_asociados.modificar_usuario
            eliminacion = permisos_asociados.eliminar_usuario

        data['crear_usuarios']=creacion
        data['modificar_usuarios']=modificacion
        data['eliminar_usuarios']=eliminacion
    """
    alumnos = Alumno.objects.all().order_by('id_alumno') #traemos todos los datos que hay en la tabla Alumno
    data['object_list'] = alumnos
    return render(request, template_name, data)

@login_required
def nuevo_alumno(request):
    """
    Vista del formulario de creacion de usuarios. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    """for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
    creacion = permisos_asociados.crear_usuario
    crear_usuarios = creacion

    if crear_usuarios==True:"""
    if request.method=='POST':
        formulario = CrearUsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.set_password(usuario.password)
            usuario.save()
            return redirect('listar_usuario')
    else:
        formulario = CrearUsuarioForm()

    return render_to_response('usuario/nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required
def editar_usuario(request, pk, template_name='usuario/editar_usuario.html'):
    """
        @param request: http request
        @param pk: id del usuario a modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de un usuario
    """
    usuario_actual = request.user
    """roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
        creacion = permisos_asociados.modificar_usuario

    modificar_usuarios = creacion
    if modificar_usuarios==True:"""
    usuario = get_object_or_404(Usuario, pk=pk)
    form = EditarUsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario')
    return render(request, template_name, {'editar_usuario': form})

@login_required
def eliminar_usuario(request, pk, template_name='usuario/eliminar_usuario.html'):
    """
    eliminar un usuario
    @param request: http request
    @param pk: id del usuario a eliminar
    @result Elimina un usuario
    +Se permite la eliminación de un usuario solo si no está asociado a ningún proyecto (si no posee ningun rol)
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    """for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
    creacion = permisos_asociados.eliminar_usuario
    eliminar_usuarios = creacion
    if eliminar_usuarios==True:"""
    server = get_object_or_404(Usuario, pk=pk)
    """lista_roles_sis = Usuario_Rol_Sistema.objects.filter(usuario = server) #vemos si existen roles de sistema asignado al usuario
    lista_roles_proy = Usuario_Rol_Proyecto.objects.filter(usuario = server) #vemos si existen roles de proyecto asignado al usuario
    count = lista_roles_sis.__len__()
    count = count + lista_roles_proy.__len__()
    if count == 0: #si count es igual a cero, entonces el usuario no posee roles asignados"""
    if request.method == 'POST':
        server.delete()
        return redirect('listar_usuario')
    """else:
        mensaje = "El usuario tiene asignado roles y no puede ser eliminado"
        return render_to_response('usuario/usuario_no_eliminado.html', {'object':mensaje}, context_instance=RequestContext(request))"""

    return render(request, template_name, {'object': server})


