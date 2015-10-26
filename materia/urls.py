# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from materia.views import listar_materias, nueva_materia, editar_materia, eliminar_materia, asignar_materia_curso, listar_materias_profesor, listar_materias_alumno


urlpatterns = patterns('',

    url(r'^$', listar_materias, name='listar_materia'),
    url(r'^listar$', listar_materias_profesor, name='listar_materias_profesor'),
    url(r'^listado$', listar_materias_alumno, name='listar_materias_alumno'),
    url(r'^nuevo$', nueva_materia, name='nueva_materia'),
    url(r'^editar/(?P<pk>\d+)$', editar_materia, name='editar_materia'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_materia, name='borrar_materia'),
    url(r'^asignar/(?P<pk>\d+)$', asignar_materia_curso, name='asignar_materia_curso'),

)
