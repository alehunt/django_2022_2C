from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def index(request):
    # Un montón de código loco
    return HttpResponse("<h1>Hola mundo!!</h1>")


def english(request):
    return HttpResponse("Hello world")


def portugues(request):
    return HttpResponse("Olá mundo")


def saludar(request, edad):
    if edad >= 40:
        saludo = "Pues como como anda?"
    else:
        saludo = "Q ace"

    return HttpResponse(f"{saludo}")
