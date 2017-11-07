from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),

    url(r'^$', views.reservacion_list, name='reservacion_list'),
    url(r'^reservacion/nueva/$', views.reservacion_nueva, name='reservacion_nueva'),
    url(r'^reservacion/(?P<pk>[0-9]+)/edit/$', views.reservacion_editar, name='reservacion_editar'),
    url(r'^reservacion/(?P<pk>\d+)/remove/$', views.reservacion_remove, name='reservacion_remove'),
    url(r'^reservacion/(?P<pk>[0-9]+)/$', views.reservacion_detail, name='reservacion_detail'),
    url(r'^cliente$', views.cliente_list, name='cliente_list'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detail, name='cliente_detail'),
    url(r'^cliente/(?P<pk>[0-9]+)/edit/$', views.cliente_edit, name='cliente_edit'),
    url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
    url(r'^cliente/(?P<pk>\d+)/remove/$', views.cliente_remove, name='cliente_remove'),
    url(r'^empleado$', views.empleado_list, name='empleado_list'),
    url(r'^empleado/new/$', views.empleado_new, name='empleado_new'),
    url(r'^empleado/(?P<pk>[0-9]+)/$', views.empleado_detail, name='empleado_detail'),
    url(r'^empleado/(?P<pk>[0-9]+)/edit/$', views.empleado_edit, name='empleado_edit'),
    url(r'^empleado/(?P<pk>\d+)/remove/$', views.empleado_remove, name='empleado_remove'),
    ]
