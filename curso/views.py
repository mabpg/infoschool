# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from curso.forms import CrearCursoForm, EditarCursoForm
from curso.models import Curso
from materia.models import Materia, Materia_curso


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
    data = {}
    cursos = Curso.objects.all().order_by('id_curso') #traemos todos los datos que hay en la tabla Curso
    data['object_list'] = cursos
    return render(request, template_name, data)


@login_required
def listar_cursos_del_profe(request, template_name='curso/listar_curso.html'):
    """
    Lista de cursos
    @param request: http request
    @param template_name nombre del template a utilizar
    @return Despliega los alumnos existentes en el sistema con sus atributos
    + Se verifican los roles y permisos de sistema asociados al usuario actual, y de acuerdo a estos
     permisos se muestran los botones a los que tiene acceso dicho usuario
    """
    data = {}
    usuario = request.user
    materias = Materia.objects.exclude(profesor=usuario) #materias que no son del profesor

    print('materias')
    print(materias)
    materias_curso = Materia_curso.objects.all()

    print("materias curso 1")
    print(materias_curso)

    for i in materias:
        materias_curso = materias_curso.exclude(materia=i)

    print("materias curso")
    print(materias_curso)

    #armamos una lista con los cursos diferentes
    cursos = []
    for i in materias_curso:
        if cursos.__contains__(i.curso)==0: #si la lista contiene ese curso entonces no el valor es 0
            cursos.append(i.curso)


    #cursos = Curso.objects.all().order_by('id_curso') #traemos todos los datos que hay en la tabla Curso
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
    server = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        server.delete()
        return redirect('listar_curso')

    return render(request, template_name, {'object': server})


