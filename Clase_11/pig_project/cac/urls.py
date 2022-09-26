from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.index),
    path('hola_mundo', views.hola_mundo),
    path('saludar/', views.saludar, name="saludar_por_defecto"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    path('proyectos/2022/09/', views.proyectos_2022_09, name='proyectos-2022-09'),
    path('proyectos/<int:anio>/<int:mes>',
         views.ver_proyectos, name="ver_proyectos"),
    path('cursos/detalle/<slug:nombre_curso>',
         views.curso_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$', views.cursos, name='cursos'),
]
