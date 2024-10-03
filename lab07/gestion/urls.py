from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('listaEventos/', views.listaEventos, name='listaEventos'),
    path('listaRegistros/', views.listaRegistros, name='listaRegistros'),
    path('crearEvento/', views.crearEvento, name='crearEvento'),
    path('actEvento/<int:evento_id>/', views.actEvento, name='actEvento'),
    path('eliminarEvento/<int:evento_id>/', views.eliminarEvento, name='eliminarEvento'),
    path('/misEventos/', views.misEventos, name='misEventos'),
    path('listarRegistros/', views.listarRegistros, name='listarRegistros'),
]
