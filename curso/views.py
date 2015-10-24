# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from curso.forms import CrearCursoForm, EditarCursoForm
from curso.models import Curso


@login_required
def listar_cursos(request, template_name='curso/listar_curso.html'):
    """
    Lista de cursos
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
    cursos = Curso.objects.all().order_by('id_curso') #traemos todos los datos que hay en la tabla Curso
    data['object_list'] = cursos
    return render(request, template_name, data)

@login_required
def nuevo_curso(request):
    """
    Vista del formulario de creacion de alumnos. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    usuario_actual = request.user
    data={}

    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    """for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
    creacion = permisos_asociados.crear_usuario
    crear_usuarios = creacion

    if crear_usuarios==True:"""
    if request.method=='POST':
        formulario = CrearCursoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_curso')
    else:
        formulario = CrearCursoForm()

    data['formulario'] = formulario
    return render_to_response('curso/nuevocurso.html', data, context_instance=RequestContext(request))


@login_required
def editar_curso(request, pk, template_name='curso/editar_curso.html'):
    """
        @param request: http request
        @param pk: id del curso a modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de un curso
    """
    usuario_actual = request.user
    """roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
        creacion = permisos_asociados.modificar_usuario

    modificar_usuarios = creacion
    if modificar_usuarios==True:"""

    data={}

    curso = get_object_or_404(Curso, pk=pk)
    form = EditarCursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('listar_curso')

    data['formulario'] = form
    return render(request, template_name, data)


@login_required
def eliminar_curso(request, pk, template_name='curso/eliminar_curso.html'):
    """
    eliminar un curso
    @param request: http request
    @param pk: id del curso a eliminar
    @result Elimina un curso
    +Se permite la eliminación de un curso solo si no está asociado a ningún proyecto (si no posee ningun rol)
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    """for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
    creacion = permisos_asociados.eliminar_usuario
    eliminar_usuarios = creacion
    if eliminar_usuarios==True:"""
    server = get_object_or_404(Curso, pk=pk)
    """lista_roles_sis = Usuario_Rol_Sistema.objects.filter(usuario = server) #vemos si existen roles de sistema asignado al usuario
    lista_roles_proy = Usuario_Rol_Proyecto.objects.filter(usuario = server) #vemos si existen roles de proyecto asignado al usuario
    count = lista_roles_sis.__len__()
    count = count + lista_roles_proy.__len__()
    if count == 0: #si count es igual a cero, entonces el usuario no posee roles asignados"""
    if request.method == 'POST':
        server.delete()
        return redirect('listar_curso')
    """else:
        mensaje = "El usuario tiene asignado roles y no puede ser eliminado"
        return render_to_response('usuario/usuario_no_eliminado.html', {'object':mensaje}, context_instance=RequestContext(request))"""

    return render(request, template_name, {'object': server})


