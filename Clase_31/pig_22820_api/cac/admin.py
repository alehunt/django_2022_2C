from django.contrib import admin

from cac.models import EstudianteM, Proyecto, CursoM, Categoria, Curso, Inscripcion, Perfil
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin

class CacAdminSite(admin.AdminSite):
    site_header = 'Adminsitración CAC'
    site_title = 'Mi admin personalizado'
    index_title = 'Administración principal'
    empty_value_display = 'No hay datos para visualizar'

# Register your models here.
#admin.site.register(Proyecto)

class EstudianteMAdmin(admin.ModelAdmin):
    list_display = ('dni_m','apellido_m','nombre_m')
    list_editable = ('nombre_m',)
    search_fields = ['apellido_m','nombre_m']
    list_filter = ('dni_m','apellido_m')



#admin.site.register(EstudianteM,EstudianteMAdmin)
class CursoMAdmin(admin.ModelAdmin):

    #modificar listado relaciones oneToMany
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'categoria':
            kwargs['queryset'] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    #modificar el listado relacion ManyToMany
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiantes':
            kwargs['queryset'] = EstudianteM.objects.filter(matricula_m__startswith="LM")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','baja')
    list_filter = ('baja',)
    # def get_queryset(self, request):
    #     query = super(CategoriaAdmin,self).get_queryset(request)
    #     filtered_query = query.filter(baja=False)
    #     return filtered_query

#SE AGREGA MODELO DE PERFIL PARA QUE SE CARGUE DESDE EL USER EN ADMIN DE DJANGO
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete= False
    verbose_name_plural= 'Perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

mi_admin = CacAdminSite(name='cacadmin')
mi_admin.register(Proyecto)
mi_admin.register(EstudianteM,EstudianteMAdmin)
mi_admin.register(User,UserAdmin)
mi_admin.register(Group,GroupAdmin)
mi_admin.register(Categoria, CategoriaAdmin)
mi_admin.register(CursoM,CursoMAdmin)
mi_admin.register(Curso)
mi_admin.register(Inscripcion)

