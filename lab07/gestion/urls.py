from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('listaEventos/', views.listaEventos, name='listaEventos'),
    path('listaRegistros/', views.listaRegistros, name='listaRegistros'),
    path('crearEvento/', views.crearEvento, name='crearEvento'),
    # path('crearRegistro/', views.crearRegistro, name='crearRegistro'),
    # path('actEvento/', views.actEvento, name='actEvento'),
    # path('actRegistro/', views.actEvento, name='actRegistro'),
]
