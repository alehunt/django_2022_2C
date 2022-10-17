from audioop import reverse
from datetime import datetime
from django.shortcuts import redirect, render
from django.conf import settings
from .forms import ContactoForm
from django.contrib import messages


def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, "hola_mundo/index.html", {"hoy": datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo})


def lenguajes(request):
    idiomas = ['English', 'Español', 'Portugues', 'Alemán']
    return render(request, "hola_mundo/lenguajes.html", {"lenguajes": idiomas})


def contacto(request):
    if request.method == "POST":
        # Creao la instancia populada con los datos cargados en pantalla
        contacto_form = ContactoForm(request.POST)
        # Valido y proceso los datos.
        if contacto_form.is_valid():
            messages.set_level(request, messages.DEBUG)
            messages.success(request, "Formulario cargado con éxito")
            messages.debug(request, "DEBUGG")
            messages.info(request, "Info importante")
            messages.warning(request, "Algo anda mal")
            messages.error(request, "NO ANDA")
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "hola_mundo/contacto.html", {'contacto_form': contacto_form})

