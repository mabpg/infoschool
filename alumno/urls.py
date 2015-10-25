# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from alumno.views import listar_alumnos, nuevo_alumno, editar_alumno, eliminar_alumno, listar_alumnos_de_profe


urlpatterns = patterns('',

    url(r'^$', listar_alumnos, name='listar_alumno'),
    url(r'^listar$', listar_alumnos_de_profe, name='listar_alumnos_de_profe'),
    url(r'^nuevo$', nuevo_alumno, name='nuevo_alumno'),
    url(r'^editar/(?P<pk>\d+)$', editar_alumno, name='editar_alumno'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_alumno, name='borrar_alumno'),

)
