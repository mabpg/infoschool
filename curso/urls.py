# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from curso.views import listar_cursos, nuevo_curso, editar_curso, eliminar_curso,listar_cursos_del_profe


urlpatterns = patterns('',

    url(r'^$', listar_cursos, name='listar_curso'),
    url(r'^listado$', listar_cursos_del_profe, name='listar_cursos_del_profe'),
    url(r'^nuevo$', nuevo_curso, name='nuevo_curso'),
    url(r'^editar/(?P<pk>\d+)$', editar_curso, name='editar_curso'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_curso, name='borrar_curso'),

)
