# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from materia.views import listar_materias, nueva_materia, editar_materia, eliminar_materia


urlpatterns = patterns('',

    url(r'^$', listar_materias, name='listar_materia'),
    url(r'^nuevo$', nueva_materia, name='nueva_materia'),
    url(r'^editar/(?P<pk>\d+)$', editar_materia, name='editar_materia'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_materia, name='borrar_materia'),

)
