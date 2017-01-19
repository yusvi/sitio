from django.conf.urls import url
from .views import *



urlpatterns = [
    #url(r'^country/$',views.CountrySerializer,name='country'),
    url(r'^get_tipo_contacto/$',get_tipo_contacto, name='get_tipo_contacto'),
    url(r'^get_organizacion/(?P<sid>[\w-]+)/$', get_organizacion, name='get_organizacion'),
    url(r'^get_contacto/(?P<cid>[\w-]+)/$', get_contacto, name='get_contacto'),
    url(r'^get_asignacion_peticion/(?P<cid>[\w-]+)/$', get_asignacion_peticion, name='get_asignacion_peticion'),
    ]
