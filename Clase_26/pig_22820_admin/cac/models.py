from ast import mod
from email.policy import default
from tabnanny import verbose
from django.db import models


class Comision(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Comsion:')
    imagen = models.ImageField(verbose_name="Imagen:", default=None, null=True)

    class Meta:
        verbose_name_plural = "Comisiones"

    def __str__(self):
        return self.nombre

    def delete(self):
        self.imagen.delete()
        return super().delete()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre:')
    apellido = models.CharField(max_length=150, verbose_name='Apellido:')
    email = models.EmailField(
        max_length=150, verbose_name='Email:', null=True, default=None)
    dni = models.BigIntegerField(verbose_name='DNI:')
    comision = models.ForeignKey(Comision, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"DNI: {self.dni} - {self.apellido}, {self.nombre}"

    def save(self, *args, **kwargs):
        if self.apellido.upper() == 'MESSI':
            raise ValueError("Messi es un maestro, no puede ser estudiante")
        else:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.apellido.upper() == 'ALMADA':
            raise ValueError("No se puede eliminar, tiene mucho que aprender")
        return super().delete(*args, **kwargs)
