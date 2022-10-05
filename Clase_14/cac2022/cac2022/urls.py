from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('', include('hola_mundo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
