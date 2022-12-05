from django.db import models
from django.utils.text import slugify 

from django.contrib.auth.models import User

#ONE TO ONE
# class Persona(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")

# class Estudiante(models.Model):
    # persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    # matricula = models.CharField(max_length=10,verbose_name='Matricula')

#Modelo Abtracto
# class PersonaAbs(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")

#     class Meta:
#         abstract=True

# class EstudianteAbs(PersonaAbs):
#     matricula = models.CharField(max_length=10,verbose_name='Matricula')

# class DocenteAbs(PersonaAbs):
#     legajo = models.CharField(max_length=10,verbose_name='Legajo')

 
class Perfil(models.Model):
    """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono')
    domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')

#HERENCIA
class PersonaM(models.Model):
    nombre_m = models.CharField(max_length=100,verbose_name='Nombre')
    apellido_m = models.CharField(max_length=150,verbose_name='Apellido')
    email_m = models.EmailField(max_length=150,null=True)
    dni_m = models.IntegerField(verbose_name="DNI")

class EstudianteM(PersonaM):
    matricula_m = models.CharField(max_length=10,verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.matricula_m} - {self.nombre_m} {self.apellido_m}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Estudiantes'

class DocenteM(PersonaM):
    legajo_m = models.CharField(max_length=10,verbose_name='Legajo')

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
        
class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion mucho a uno    
    estudiantes = models.ManyToManyField(EstudianteM,through='Inscripcion') #related_name="cursos"

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()

class CursoM(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion mucho a uno    
    estudiantes = models.ManyToManyField(EstudianteM) #related_name="cursos"

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()
        
class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(EstudianteM, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.estudiante.nombre_m

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    anio = models.IntegerField(verbose_name='Año')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    url = models.URLField(max_length=100,verbose_name='Url')
    portada = models.ImageField(upload_to='imagenes/proyecto/',null=True,verbose_name='Portada')    
    estudiante = models.ForeignKey(EstudianteM,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    """ Sobreescribo el metodo save del modelo"""
    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()
