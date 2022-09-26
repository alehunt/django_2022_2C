from cgitb import reset
import re
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect


def index(request):
    if (request.method == 'GET'):
        titulo = 'Titulo cuando accedo por get'
    else:
        titulo = f'Titulo cuando accedo por otro metodo'
    parameters_get = request.GET.get('algo')
    return render(request, 'index.html', {'titulo': titulo, 'parametro': parameters_get})

# Create your views here.


def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')


def saludar(request, nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
        <p>Estoy haciendo mi primera prueba</p>
    """)


def ver_proyectos(request, anio, mes):
    return HttpResponse(f"""
        <h1>Proyectos del  - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)


def proyectos_2022_09(request):
    return redirect(reverse('saludar_por_defecto'))


def cursos(request, nombre):
    return HttpResponse(f'{nombre}')


def curso_detalle(request, nombre_curso):
    return HttpResponse(f'{nombre_curso}')
