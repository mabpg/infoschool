# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from usuario.forms import CrearUsuarioForm, EditarUsuarioForm, EditarPerfilForm
from usuario.models import Usuario
from alumno.models import Alumno


@login_required
def listar_usuarios(request, template_name='usuario/listar_usuario.html'):
    """
    Lista de usuarios
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los usuarios existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    data = {}

    usuarios = Usuario.objects.all().order_by('id_usuario') #traemos todos los datos que hay en la tabla Usuarios
    data['object_list'] = usuarios
    return render(request, template_name, data)


@login_required
def perfil_usuario(request, template_name='usuario/perfil_usuario.html'):
    """
    Lista de usuarios
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los usuarios existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    data = {}
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id_usuario) #traemos todos los datos que hay en la tabla Usuarios

    if usuario.clase=="Alumno" and usuario.is_admin==False:
        alumno = Alumno.objects.get(usuario=usuario)
        data['curso'] = True
        data['alumno'] = alumno.curso.nombre+' '+alumno.curso.especialidad

    data['usuario'] = usuario
    return render(request, template_name, data)

@login_required
def editar_perfil(request, pk, template_name='usuario/editar_perfil.html'):
    """
        @param request: http request
        @param pk: id del usuario a modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de un usuario
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    form = EditarPerfilForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('perfil_usuario')
    return render(request, template_name, {'editar_usuario': form})



@login_required
def nuevo_usuario(request):
    """
    Vista del formulario de creacion de usuarios. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """

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

    server = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        server.delete()
        return redirect('listar_usuario')

    return render(request, template_name, {'object': server})


