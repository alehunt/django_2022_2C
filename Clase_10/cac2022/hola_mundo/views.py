from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hola gente")


def hello(request):
    return HttpResponse("Hello world")


def ola(request):
    return HttpResponse("Olá mundo")


def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre.upper()}")
