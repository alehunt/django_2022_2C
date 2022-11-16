from django.contrib import admin
from cac.models import Estudiante, Comision


class EstudianteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estudiante, EstudianteAdmin)
# admin.site.register(Comision)

@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    pass


