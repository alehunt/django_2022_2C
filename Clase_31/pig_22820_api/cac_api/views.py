from rest_framework import viewsets
from rest_framework import permissions
from cac.models import EstudianteM
from cac_api import serializers


# Create your views here.
class EstudianteMViewSet(viewsets.ModelViewSet):
    queryset = EstudianteM.objects.all().order_by('id')
    serializer_class = serializers.EstudianteMSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
