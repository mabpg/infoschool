# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from anotacion.views import listar_anotaciones, nueva_anotacion, editar_anotacion, eliminar_anotacion, completar_agregar_anotacion


urlpatterns = patterns('',

    url(r'^$', listar_anotaciones, name='listar_anotacion'),
    url(r'^nuevo$', nueva_anotacion, name='nueva_anotacion'),
    url(r'^editar/(?P<pk>\d+)$', editar_anotacion, name='editar_anotacion'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_anotacion, name='borrar_anotacion'),
    url(r'^asignar/(?P<pk>\d+)$', completar_agregar_anotacion, name='completar_agregar_anotacion'),

)
