# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from usuario.views import eliminar_usuario, editar_usuario, listar_usuarios, nuevo_usuario, perfil_usuario, editar_perfil


urlpatterns = patterns('',

    url(r'^$', listar_usuarios, name='listar_usuario'),
    url(r'^listar$', perfil_usuario, name='perfil_usuario'),
    url(r'^editar/perfil/(?P<pk>\d+)$', editar_perfil, name='editar_perfil'),
    url(r'^nuevo$', nuevo_usuario, name='nuevo_usuario'),
    url(r'^editar/(?P<pk>\d+)$', editar_usuario, name='editar_usuario'),
    url(r'^borrar/(?P<pk>\d+)$', eliminar_usuario, name='borrar_usuario'),

)
