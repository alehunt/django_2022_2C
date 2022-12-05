from rest_framework import serializers
from cac.models import EstudianteM


class EstudianteMSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteM
        fields = ['id', 'nombre_m', 'apellido_m', 'email_m', 'dni_m', 'matricula_m']
