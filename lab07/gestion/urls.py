from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('listaEventos/', views.listaEventos, name='listaEventos'),
    path('listaRegistros/', views.listaRegistros, name='listaRegistros'),
    path('crearEvento/', views.crearEvento, name='crearEvento'),
    path('actEvento/<int:evento_id>/', views.actEvento, name='actEvento'),
    path('eliminarEvento/<int:evento_id>/', views.eliminarEvento, name='eliminarEvento'),
    path('misEventos/', views.misEventos, name='misEventos'),
    path('listarRegistros/', views.listarRegistros, name='listarRegistros'),
    path('menuConsultas/', views.menuConsultas, name='menuConsultas'),
    path('consultaUsuarios/', views.consultaUsuarios, name='consultaUsuarios'),
    path('consultaOrganizacion/', views.consultaOrganizacion, name='consultaOrganizacion'),
    path('consultaEventos/', views.consultaEventos, name='consultaEventos'),
    
]
