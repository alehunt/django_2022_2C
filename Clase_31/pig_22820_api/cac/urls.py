from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='inicio'),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('proyectos/',views.ver_proyectos, name='proyectos'),
    path('cursos/',views.ver_cursos, name='cursos'),
    path('api_proyectos/',views.api_proyectos,name="api_proyectos"),
    
    path('administracion/', views.index_administracion,name='inicio_administracion'),

    path('administracion/categorias', views.CategoriaListView.as_view(),name='categorias_index'),
    # path('administracion/categorias/nuevo', views.categorias_nuevo,name='categorias_nuevo'),
    path('administracion/categorias/nuevo', views.CategoriaView.as_view(),name='categorias_nuevo'),
    path('administracion/categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('administracion/categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),

    path('administracion/cursos', views.cursos_index,name='cursos_index'),
    path('administracion/cursos/nuevo/', views.cursos_nuevo,name='cursos_nuevo'),
    path('administracion/cursos/editar/<int:id_curso>', views.cursos_editar,name='cursos_editar'),
    path('administracion/cursos/eliminar/<int:id_curso>', views.cursos_eliminar,name='cursos_eliminar'),
    
    path('administracion/estudiantes', views.estudiantes_index,name='estudiantes_index'),
    path('administracion/estudiantes/nuevo/', views.estudiantes_nuevo,name='estudiantes_nuevo'),
    path('administracion/estudiantes/editar/<int:id_estudiante>', views.estudiantes_editar,name='estudiantes_editar'),
    path('administracion/estudiantes/eliminar/<int:id_estudiante>', views.estudiantes_eliminar,name='estudiantes_eliminar'),
    
    path('administracion/proyectos', views.proyectos_index,name='proyectos_index'),
    path('administracion/proyectos/nuevo/', views.proyectos_nuevo,name='proyectos_nuevo'),
    path('administracion/proyectos/editar/<int:id_proyecto>', views.proyectos_editar,name='proyectos_editar'),
    path('administracion/proyectos/eliminar/<int:id_proyecto>', views.proyectos_eliminar,name='proyectos_eliminar'),


    # path('cuentas/login/', views.cac_login,name='login'),
    # path('cuentas/login/', views.CacLoginView.as_view(),name='login'),
    # path('cuentas/logout/',
        #  auth_views.LogoutView.as_view(template_name='cac/publica/index.html'), name='logout'),
    path('cuentas/registrarse', views.cac_registrarse, name='registrarse'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name='cac/publica/login.html')),
    # path('account/logout/',
    #      auth_views.LogoutView.as_view(template_name='cac/publica/logout.html'), name='logout'),
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(success_url='/')),
    path('accounts/',include('django.contrib.auth.urls')),


    path('hola_mundo',views.hola_mundo),
    path('saludarbonito/',views.saludar,name="saludar_por_defecto"),
    path('saludar/<str:nombre>',views.saludar,name="saludar"),
    # path('proyectos/2022/07',views.ver_proyectos_2022_07),
    # re_path(r'^proyectos/(?P<anio>\d{2,4})/$',views.ver_proyectos),
    # path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos"),
    # path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    # re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
