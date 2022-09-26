from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


# Create your views here.
def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hola gente</h1>")


def hello(request):
    return HttpResponse("Hello world")


def ola(request):
    return HttpResponse("Olá mundo")


def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre.upper()}")
