# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from alumno.forms import CrearAlumnoForm, EditarAlumnoForm
from alumno.models import Alumno
from usuario.models import Usuario
from curso.models import Curso
from materia.models import Materia, Materia_curso


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
    data = {}
    data['admin'] = False
    data['alum'] = False
    data['profe'] = False
    if(usuario_actual.is_admin==True):
        data['admin']=True

    if(usuario_actual.clase=='Alumno'):
        data['alum']=True

    if(usuario_actual.clase=='Profesor'):
        data['profe']=True

    alumnos = Alumno.objects.all().order_by('id_alumno') #traemos todos los datos que hay en la tabla Alumno
    data['object_list'] = alumnos
    return render(request, template_name, data)


@login_required
def listar_alumnos_de_profe(request, template_name='alumno/listar_alumnos_del_profe.html'):
    """
    Lista de alumnos
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user
    data = {}
    data['admin'] = False
    data['alum'] = False
    data['profe'] = False
    if(usuario_actual.is_admin==True):
        data['admin']=True

    if(usuario_actual.clase=='Alumno'):
        data['alum']=True

    if(usuario_actual.clase=='Profesor'):
        data['profe']=True

    materias_no_del_profe = Materia.objects.exclude(profesor=usuario_actual)

    todas_materias_curso = Materia_curso.objects.all()

    for i in materias_no_del_profe:
        todas_materias_curso = todas_materias_curso.exclude(materia=i)

    todos_los_cursos = Curso.objects.all()
    for i in todas_materias_curso:
         todos_los_cursos = todos_los_cursos.exclude(id_curso=i.curso.id_curso)     #todos los no cursos

    alumnos = Alumno.objects.all() #traemos todos los datos que hay en la tabla Alumno

    for i in todos_los_cursos:
        alumnos=alumnos.exclude(curso=i)

    data['object_list'] = alumnos
    return render(request, template_name, data)

@login_required
def nuevo_alumno(request):
    """
    Vista del formulario de creacion de alumnos. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    usuarios = Usuario.objects.all().exclude(clase='Profesor')      #Traemos todos los usuarios que son alumnos

    for i in usuarios:
        if i.is_admin:
            usuarios = usuarios.exclude(id_usuario=i.id_usuario)

    alumnos = Alumno.objects.all()                                  #traemos todos los elementos de la tabla alumno

    usuarios_finales = usuarios

    for i in alumnos:   #quitamos los usuarios que ya están en la tabla alumno
        usuarios_finales = usuarios_finales.exclude(id_usuario=i.usuario.id_usuario)

    data = {}
    data['hay_mns'] = False
    if usuarios_finales.__len__() == 0:
        data['hay_mns'] = True

    data['usuarios'] = list(usuarios_finales)


    cursos = Curso.objects.all()      #Traemos todos los cursos
    data['cursos'] = list(cursos)

    if request.method=='POST':
        formulario = CrearAlumnoForm(request.POST)
        if formulario.is_valid():
            id_curso = request.POST['curso']
            curso = Curso.objects.get(id_curso=id_curso)

            id_usuario_alumno = request.POST['usuario']
            usuario = Usuario.objects.get(id_usuario=id_usuario_alumno)
            alumno = formulario.save()
            alumno.usuario=usuario
            alumno.curso=curso
            alumno.save()
            return redirect('listar_alumno')
    else:
        formulario = CrearAlumnoForm()

    data['formulario']=formulario
    return render_to_response('alumno/nuevoalumno.html', data, context_instance=RequestContext(request))

@login_required
def editar_alumno(request, pk, template_name='alumno/editar_alumno.html'):
    """
        @param request: http request
        @param pk: id del alumno a modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de un alumno
    """
    usuario_actual = request.user
    alumnos = Alumno.objects.all()                                  #traemos todos los elementos de la tabla alumno

    data={}
    data['alumnos']=alumnos

    cursos = Curso.objects.all()      #Traemos todos los cursos
    data['cursos'] = list(cursos)

    alumno = get_object_or_404(Alumno, pk=pk)
    form = EditarAlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save()
        return redirect('listar_alumno')

    data['formulario'] = form
    return render(request, template_name, data)

@login_required
def eliminar_alumno(request, pk, template_name='alumno/eliminar_alumno.html'):
    """
    eliminar un alumno
    @param request: http request
    @param pk: id del alumno a eliminar
    @result Elimina un alumno
    +Se permite la eliminación de un alumno solo si no está asociado a ningún proyecto (si no posee ningun rol)
    """
    usuario_actual = request.user

    server = get_object_or_404(Alumno, pk=pk)

    if request.method == 'POST':
        server.delete()
        return redirect('listar_alumno')

    return render(request, template_name, {'object': server})


