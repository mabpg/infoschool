# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from materia.forms import CrearMateriaForm, EditarMateriaForm, AsignarMateriaCursoForm
from usuario.models import Usuario
from materia.models import Materia, Materia_curso
from curso.models import Curso
from alumno.models import Alumno

@login_required
def listar_materias(request, template_name='materia/listar_materia.html'):
    """
    Lista de materias
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user
    data = {}

    materias = Materia.objects.all().order_by('id_materia') #traemos todos los datos que hay en la tabla Materia
    data['object_list'] = materias
    return render(request, template_name, data)

@login_required
def listar_materias_profesor(request, template_name='materia/listar_materias_profesor.html'):
    """
    Lista de materias
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user

    data = {}
    materias_del_profe = Materia.objects.filter(profesor=usuario_actual)

    data['object_list'] = materias_del_profe
    return render(request, template_name, data)

@login_required
def listar_materias_alumno(request, template_name='materia/listar_materias_alumno.html'):
    """
    Lista de materias
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    usuario_actual = request.user

    data = {}
    alumno = Alumno.objects.get(usuario=usuario_actual)
    materias_del_alumno = Materia_curso.objects.filter(curso=alumno.curso)
    data['object_list'] = materias_del_alumno
    return render(request, template_name, data)

@login_required
def nueva_materia(request):
    """
    Vista del formulario de creacion de materias. Ver forms.py
    @param request: http request
    Permite crear usuarios a partir de un formulario
    @return Crea un usuario nuevo
    +Además de crear un usuario se verifica que el usuario que trata de acceder a está funcionalidad tenga el permiso
    correspondiente
    """
    usuario_actual = request.user
    profesores = Usuario.objects.all().exclude(clase='Alumno')      #Traemos todos los usuarios que son profesores

    data={}
    data['profes'] = profesores

    if request.method=='POST':
        formulario = CrearMateriaForm(request.POST)
        if formulario.is_valid():

            id_usuario_profesor = request.POST['profesor']
            usuario = Usuario.objects.get(id_usuario=id_usuario_profesor)
            materia = formulario.save()
            materia.profesor=usuario
            materia.save()

            return redirect('listar_materia')
    else:
        formulario = CrearMateriaForm()

    data['formulario'] = formulario
    return render_to_response('materia/nuevamateria.html', data, context_instance=RequestContext(request))


@login_required
def editar_materia(request, pk, template_name='materia/editar_materia.html'):
    """
        @param request: http request
        @param pk: id de la materia a modificar
        @param template_name nombre del template a utilizar
        @result Modifica los campos de una materia
    """
    usuario_actual = request.user
    profesores = Usuario.objects.all().exclude(clase='Alumno')      #Traemos todos los usuarios que son profesores

    data={}
    data['profes'] = profesores
    materia = get_object_or_404(Materia, pk=pk)
    form = EditarMateriaForm(request.POST or None, instance=materia)
    if form.is_valid():
        form.save()
        return redirect('listar_materia')

    data['formulario'] = form
    return render(request, template_name, data)


@login_required
def eliminar_materia(request, pk, template_name='materia/eliminar_materia.html'):
    """
    eliminar una materia
    @param request: http request
    @param pk: id de la materia eliminar
    @result Elimina una materia
    +Se permite la eliminación de una materia solo si no está asociado a ningún proyecto (si no posee ningun rol)
    """

    server = get_object_or_404(Materia, pk=pk)

    if request.method == 'POST':
        server.delete()
        return redirect('listar_materia')

    return render(request, template_name, {'object': server})

@login_required
def asignar_materia_curso(request, pk, template_name='materia/asignar_materia_curso.html'):

    """
        Asignar roles a usuarios
        @param request: http request
        @param pk: id de la materia a asignar
        @param template_name nombre del template a utilizar
        @return asigna roles a un usuario
        + Se asignan roles de sistema a un usuario, Un mismo usuario no puede asignarse roles a sí mismo
    """
    data={}
    materia = get_object_or_404(Materia, id_materia=pk)
    cursos_ya_asignados = Materia_curso.objects.filter(materia=materia)
    print(cursos_ya_asignados)
    todos_cursos = Curso.objects.all()


    for i in cursos_ya_asignados:
        todos_cursos = todos_cursos.exclude(id_curso=i.curso.id_curso)

    data['hay_elementos']=False


    if(todos_cursos.__len__()>0):
        data['hay_elementos']=True


    data['cursos'] = todos_cursos
    data['materia'] = pk
    formulario = AsignarMateriaCursoForm(request.POST or None)

    if formulario.is_valid():
        form = formulario.save()
        form.materia = materia
        form.save()
        return redirect('listar_materia')

    return render(request, template_name, data)


