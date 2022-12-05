from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cac_api import views

router = DefaultRouter()
router.register(r'estudiantes', views.EstudianteMViewSet, basename='estudiante')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
