# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from anotacion.views import listar_anotaciones, nueva_anotacion, editar_anotacion, eliminar_anotacion, completar_agregar_anotacion, listar_anotaciones_alumno, nueva_anotacion_alumno, completar_agregar_anotacion_alumno


urlpatterns = patterns('',

    url(r'^$', listar_anotaciones, name='listar_anotacion'),
    url(r'^listado/(?P<pk>\d+)$', listar_anotaciones_alumno, name='listar_anotaciones_alumno'),
    url(r'^nueva/anotacion/(?P<pk>\d+)$', nueva_anotacion_alumno, name='nueva_anotacion_alumno'),
    url(r'^nuevo$', nueva_anotacion, name='nueva_anotacion'),
    url(r'^editar/(?P<pk>\d+)$', editar_anotacion, name='editar_anotacion'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_anotacion, name='borrar_anotacion'),
    url(r'^asignar/(?P<pk>\d+)$', completar_agregar_anotacion, name='completar_agregar_anotacion'),
    url(r'^asignar/(?P<pk>\d+)/(?P<id_al>\d+)$', completar_agregar_anotacion_alumno, name='completar_agregar_anotacion_alumno'),



)
