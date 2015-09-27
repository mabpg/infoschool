# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from alumno.views import listar_alumnos, nuevo_alumno, editar_alumno, eliminar_alumno


urlpatterns = patterns('',

    url(r'^$', listar_alumnos, name='listar_alumno'),
    url(r'^nuevo$', nuevo_alumno, name='nuevo_alumno'),
    url(r'^editar/(?P<pk>\d+)$', editar_alumno, name='editar_alumno'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_alumno, name='borrar_alumno'),

)
