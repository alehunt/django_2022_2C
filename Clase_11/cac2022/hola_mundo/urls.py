from django.urls import path
from hola_mundo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('english', views.hello, name="hello"),
    path('portuguese', views.ola, name='ola'),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    ]
