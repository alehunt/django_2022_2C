from django.http import HttpResponse


def url_invalida(request):
    return HttpResponse("Url INVALIDA", status=404)
