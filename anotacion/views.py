# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from anotacion.forms import CrearAnotacionForm, EditarAnotacionForm, AsignarMateriaForm
from materia.models import Materia, Materia_curso
from anotacion.models import Anotacion
from alumno.models import Alumno

@login_required
def listar_anotaciones(request, template_name='anotacion/listar_anotacion.html'):
    """
    Lista de anotaciones
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    data = {}

    anotaciones = Anotacion.objects.all().order_by('id_anotacion') #traemos todos los datos que hay en la tabla Anotacion
    data['object_list'] = anotaciones
    return render(request, template_name, data)

@login_required
def listar_anotaciones_alumno(request, pk, template_name='anotacion/listar_anotacion_alumno.html'):
    """
    Lista de anotaciones
    @param request: http request
    @param pk: es el id del alumno
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """

    data = {}
    alumno = Alumno.objects.get(id_alumno=pk)
    anotaciones = Anotacion.objects.filter(alumno=alumno)
    data['object_list'] = anotaciones
    data['id_alumno'] = pk
    return render(request, template_name, data)

@login_required
def nueva_anotacion(request):
    """
    Vista del formulario de creacion de anotaciones. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    data = {}
    usuario_actual = request.user
    alumnos = Alumno.objects.all()      #Traemos todos los alumnos
    data['alumnos'] = list(alumnos)

    if request.method=='POST':
        formulario = CrearAnotacionForm(request.POST)
        if formulario.is_valid():
            id_alumno = request.POST['alumno']
            alumno = Alumno.objects.get(id_alumno=id_alumno)
            form = formulario.save()
            form.alumno=alumno
            form.save()
            id_anotacion=form.id_anotacion
            #return redirect('listar_anotacion')
            return redirect('completar_agregar_anotacion', id_anotacion)
    else:
        formulario = CrearAnotacionForm()

    data['formulario']=formulario
    data['alumnos'] = list(alumnos)
    return render_to_response('anotacion/nuevaanotacion.html', data, context_instance=RequestContext(request))


@login_required
def nueva_anotacion_alumno(request, pk):
    """
    Vista del formulario de creacion de anotaciones. Ver forms.py
    @param request: http request
    @param pk: id del alumno
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    data = {}
    usuario_actual = request.user
    alumno = Alumno.objects.get(id_alumno=pk)


    if request.method=='POST':
        formulario = CrearAnotacionForm(request.POST)
        if formulario.is_valid():

            form = formulario.save()
            form.alumno=alumno
            form.save()
            id_anotacion=form.id_anotacion

            return redirect('completar_agregar_anotacion_alumno', id_anotacion, pk)
    else:
        formulario = CrearAnotacionForm()

    data['formulario']=formulario
    data['id_alumno'] = pk

    return render_to_response('anotacion/nueva_anotacion_alumno.html', data, context_instance=RequestContext(request))

@login_required
def completar_agregar_anotacion(request, pk, template_name='anotacion/completar_anotacion.html'):
    """
            @param request: http request
            @param pk: id de la anotacion
            @param template_name nombre del template a utilizar
            @result se agrega materia y responsable de la anotacion
    """
    anotacion = Anotacion.objects.get(id_anotacion=pk)
    curso=anotacion.alumno.curso
    materia_del_curso=Materia_curso.objects.filter(curso=curso)

    materias=[]
    for i in materia_del_curso:
        materias.append(i.materia)

    data={}
    data['materias'] = materias
    data['anotacion'] = pk

    form = AsignarMateriaForm(request.POST or None, instance=anotacion)
    if form.is_valid():
        id_materia = request.POST['materia']
        form.materia = id_materia
        form.save()
        return redirect('listar_anotacion')

    data['formulario'] = form
    return render(request, template_name, data)



@login_required
def completar_agregar_anotacion_alumno(request, pk, id_al, template_name='anotacion/completar_anotacion_alumno.html'):
    """
            @param request: http request
            @param pk: id de la anotacion
            @param id_al: id del alumno
            @param template_name nombre del template a utilizar
            @result se agrega materia y responsable de la anotacion
    """
    anotacion = Anotacion.objects.get(id_anotacion=pk)
    curso=anotacion.alumno.curso
    materia_del_curso=Materia_curso.objects.filter(curso=curso)

    materias=[]
    for i in materia_del_curso:
        materias.append(i.materia)

    data={}
    data['materias'] = materias
    data['anotacion'] = pk
    data['id_al'] = id_al

    form = AsignarMateriaForm(request.POST or None, instance=anotacion)
    if form.is_valid():
        id_materia = request.POST['materia']
        form.materia = id_materia
        form.save()
        return redirect('listar_anotaciones_alumno', id_al)

    data['formulario'] = form
    return render(request, template_name, data)


@login_required
def editar_anotacion(request, pk, template_name='anotacion/editar_anotacion.html'):
    """
        @param request: http request
        @param pk: id de la anotacion modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de una anotacion
    """


    usuario_actual = request.user
    anotacion = get_object_or_404(Anotacion, pk=pk)
    curso=anotacion.alumno.curso
    materia_del_curso=Materia_curso.objects.filter(curso=curso)

    materias=[]
    for i in materia_del_curso:
        materias.append(i.materia)

    data={}
    data['materias'] = materias
    data['alumno'] = False

    form = EditarAnotacionForm(request.POST or None, instance=anotacion)
    if form.is_valid():

        form.save()
        return redirect('listar_anotacion')

    data['formulario'] = form
    return render(request, template_name, data)

@login_required
def editar_anotacion_alumno(request, pk, id_al, template_name='anotacion/editar_anotacion.html'):
    """
        @param request: http request
        @param pk: id de la anotacion modificar
        @param id_al: id del alumno
        @param template_name nombre del template a utilizar
        @result Modifica los campos de una anotacion
    """
    usuario_actual = request.user
    anotacion = get_object_or_404(Anotacion, pk=pk)
    curso=anotacion.alumno.curso
    materia_del_curso=Materia_curso.objects.filter(curso=curso)

    materias=[]
    for i in materia_del_curso:
        materias.append(i.materia)

    data={}
    data['materias'] = materias
    data['alumno'] = True
    data['id_al'] = id_al

    form = EditarAnotacionForm(request.POST or None, instance=anotacion)
    if form.is_valid():

        form.save()
        return redirect('listar_anotaciones_alumno', id_al)

    data['formulario'] = form
    return render(request, template_name, data)


@login_required
def eliminar_anotacion(request, pk, template_name='anotacion/eliminar_anotacion.html'):
    """
    eliminar una anotacion
    @param request: http request
    @param pk: id de la anotacion a eliminar
    @result Elimina una anotacion
    +Se permite la eliminación de una anotacion solo si no está asociado a ningún proyecto (si no posee ningun rol)
    """
    usuario_actual = request.user
    #roles_sistema_usuarios = list(Usuario_Rol_Sistema.objects.filter(usuario=usuario_actual)) #traemos todos los roles de sistema que se han asignado al usuario en cuestion
    """for i in roles_sistema_usuarios:
        permisos_asociados = i.roles.permiso_sistema
    creacion = permisos_asociados.eliminar_usuario
    eliminar_usuarios = creacion
    if eliminar_usuarios==True:"""
    server = get_object_or_404(Anotacion, pk=pk)
    """lista_roles_sis = Usuario_Rol_Sistema.objects.filter(usuario = server) #vemos si existen roles de sistema asignado al usuario
    lista_roles_proy = Usuario_Rol_Proyecto.objects.filter(usuario = server) #vemos si existen roles de proyecto asignado al usuario
    count = lista_roles_sis.__len__()
    count = count + lista_roles_proy.__len__()
    if count == 0: #si count es igual a cero, entonces el usuario no posee roles asignados"""
    if request.method == 'POST':
        server.delete()
        return redirect('listar_anotacion')
    """else:
        mensaje = "El usuario tiene asignado roles y no puede ser eliminado"
        return render_to_response('usuario/usuario_no_eliminado.html', {'object':mensaje}, context_instance=RequestContext(request))"""

    return render(request, template_name, {'object': server})


