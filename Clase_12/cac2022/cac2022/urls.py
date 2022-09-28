from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', include('hola_mundo.urls')),
]