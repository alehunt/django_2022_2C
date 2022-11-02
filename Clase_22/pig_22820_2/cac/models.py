from email.policy import default
from tabnanny import verbose
from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')


class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, primary_key=True, on_delete=models.CASCADE)
    legajo = models.CharField(max_length=100, verbose_name='Legajo')


# class Docente(Persona):
#     cuit = models.CharField(max_length=100, verbose_name='Cuit')


# class Categoria(models.Model):
#     nombre = models.CharField(max_length=50, verbose_name='Nombre')
#     baja = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nombre

#     def soft_delete(self):
#         self.baja = True
#         self.save()

#     def restore(self):
#         self.baja = False
#         self.save()


# class Curso(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     # descripcion = models.TextField(null=True, verbose_name='Descripcion')
#     # fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
#     # portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Portada')
#     # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#     # estudiantes = models.ManyToManyField(Estudiante)

#     def __str__(self):
#         return self.nombre


# class Estudiante(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='Nombre')
#     # apellido = models.CharField(max_length=150, verbose_name='Apellido')
#     cursos = models.ManyToManyField(Curso)

#     def __str__(self):
#         return self.nombre