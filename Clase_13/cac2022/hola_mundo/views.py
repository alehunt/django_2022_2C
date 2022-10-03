from datetime import datetime
from django.shortcuts import render
from django.conf import settings


def index(request):
    saludos = ['Hola', 'Hello', 'Olá']
    idioma_saludo = {'en': 'hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, "hola_mundo/index.html", {"hoy": datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo, "media": settings.MEDIA_ROOT})


def lenguajes(request):
    idiomas = ['English', 'Español', 'Portugues']
    return render(request, "hola_mundo/lenguajes.html", {"lenguajes": idiomas})
