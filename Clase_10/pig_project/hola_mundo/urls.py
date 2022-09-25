from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('english/', views.english),
    path('portugues/', views.portugues),
    path('saludar/<int:edad>', views.saludar)
]
