from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal.views import ingresar, recuperar_contrasenha, home_sistema

urlpatterns = patterns('',

    url(r'^$', ingresar,name='ingresar'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^cerrar/$', 'principal.views.cerrar', name='cerrar_sesion'),
    url(r'^recuperar/$', recuperar_contrasenha,name='recuperar_contrasenha'),
    url(r'^home/$', home_sistema, name='home_sistema'),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^alumno/', include('alumno.urls')),
    url(r'^materia/', include('materia.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
