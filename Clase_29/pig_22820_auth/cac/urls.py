from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/registrarse', views.cac_registrarse, name='registrarse'),
    path('accounts/', include('django.contrib.auth.urls')),
    #     path('cuentas/login', views.cac_login, name='login'),
    #     path('cuentas/logout/',
    #          auth_views.LogoutView.as_view(template_name='cac/publica/index.html'), name='logout'),
    path('quienessomos/', views.quienes_somos, name='quienes_somos'),
    path('proyectos/', views.ver_proyectos, name='proyectos'),
    path('cursos/', views.ver_cursos, name='cursos'),
    path('administracion', views.index_administracion,
         name='inicio_administracion'),

    path('administracion/estudiantes/editar/<int:id_estudiante>',
         views.estudiantes_editar, name='estudiantes_editar'),
    path('administracion/estudiantes/eliminar/<int:id_estudiante>',
         views.estudiantes_eliminar, name='estudiantes_eliminar'),
    path('administracion/estudiantes/nuevo/',
         views.EstudiantesView.as_view(), name='estudiantes_nuevo'),
    path('administracion/estudiantes',
         views.EstudiantesListView.as_view(), name='estudiantes_index'),

    path('api_proyectos/', views.api_proyectos, name="api_proyectos"),

    path('hola_mundo', views.hola_mundo),
    path('saludarbonito/', views.saludar, name="saludar_por_defecto"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    # path('proyectos/2022/07',views.ver_proyectos_2022_07),
    # re_path(r'^proyectos/(?P<anio>\d{2,4})/$',views.ver_proyectos),
    # path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos"),
    # path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    # re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")
    path('', views.index, name='inicio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
