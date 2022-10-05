from datetime import datetime
from django.shortcuts import render
from django.conf import settings


def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, "hola_mundo/index.html", {"hoy": datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo})


def lenguajes(request):
    idiomas = ['English', 'Español', 'Portugues', 'Alemán']
    return render(request, "hola_mundo/lenguajes.html", {"lenguajes": idiomas})
