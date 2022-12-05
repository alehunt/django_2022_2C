from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader

from cac.forms import ContactoForm, CategoriaForm, CursoForm, CategoriaFormValidado, EstudianteMForm,ProyectoForm,RegistrarUsuarioForm

from cac.models import Categoria, Curso, EstudianteM, Proyecto

from django.contrib import messages


from django.views.generic import ListView
from django.views import View


from django.core.mail import send_mail
from django.conf import settings


from  django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required, permission_required

# from django.contrib.auth.views import LoginView

"""
    Vistas de la parte pública
"""
def index(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):
            #enviar un email al administrado con los datos
            #guardar los datos en la base
            messages.success(request,'Muchas gracias por contactarte, te esteremos respondiendo en breve.')
            messages.info(request,'Otro mensajito')
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f"""
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
            """
            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            )
            #deberia validar y realizar alguna accion
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        contacto_form = ContactoForm()

    return render(request,'cac/publica/index.html',
                {'cursos':listado_cursos,'contacto_form':contacto_form})

def quienes_somos(request):
    #return redirect('saludar_por_defecto')
    #return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('cac/publica/quienes_somos.html')
    context = {'titulo':'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))
    
def ver_proyectos(request,anio=2022,mes=1):
    proyectos = []
    return render(request,'cac/publica/proyectos.html',{'proyectos':proyectos})

@login_required(login_url=settings.LOGIN_URL)
def ver_cursos(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'cac/publica/cursos.html',{'cursos':listado_cursos})

def api_proyectos(request,):
    proyectos = [{
        'autor': 'Gustavo Villegas',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/12/Gustavo-Martin-Villegas-300x170.png',
        'url':'https://marvi-artarg.web.app/'
    },{
        'autor': 'Enzo Martín Zotti',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Enzo-Martin-Zotti-300x170.jpg',
        'url':'https://hablaconmigo.com.ar/'
    },{
        'autor': 'María Echevarría',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Maria-Echevarria-300x170.jpg',
        'url':'https://compassionate-colden-089e8a.netlify.app/'
    },]
    response = {'status':'Ok','code':200,'message':'Listado de proyectos','data':proyectos}
    return JsonResponse(response,safe=False)
 
"""
    Vistas de la parte administracion
"""
@login_required(login_url=settings.LOGIN_URL)
def index_administracion(request):
    #EJEMPLO DE CONSULTA SI UN USUARIO PERTENECE A UN GRUPO
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'cac/administracion/403_admin.html')
    variable = 'test variable'
    return render(request,'cac/administracion/index_administracion.html',{'variable':variable})

"""
    CRUD Categorias
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_categoria', login_url=settings.LOGIN_URL)
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'cac/administracion/categorias/index.html',{'categorias':categorias})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_categoria', login_url=settings.LOGIN_URL)
def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado()
    return render(request,'cac/administracion/categorias/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_categoria', login_url=settings.LOGIN_URL)
def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaFormValidado(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaFormValidado(instance=categoria)
    return render(request,'cac/administracion/categorias/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_categoria', login_url=settings.LOGIN_URL)
def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')

"""
    CRUD Cursos
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_curso', raise_exception=True) #envia una exception 403
def cursos_index(request):
    cursos = Curso.objects.all()
    return render(request,'cac/administracion/cursos/index.html',{'cursos':cursos})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_curso', login_url=settings.LOGIN_URL)
def cursos_nuevo(request):
    #forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    formulario = CursoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'cac/administracion/cursos/nuevo.html',{'formulario':formulario})


@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_curso',  raise_exception=True)
def cursos_editar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = CursoForm(request.POST or None,request.FILES or None,instance=curso)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'cac/administracion/cursos/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_curso', login_url=settings.LOGIN_URL)
def cursos_eliminar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el curso correctamente')          
    curso.delete()
    return redirect('cursos_index')

"""
    CRUD Estudiantes
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_index(request):
    estudiantes = EstudianteM.objects.all()
    return render(request,'cac/administracion/estudiantes/index.html',{'estudiantes':estudiantes})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_nuevo(request):
    formulario = EstudianteMForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'cac/administracion/estudiantes/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_editar(request,id_estudiante):
    try:
        estudiante = EstudianteM.objects.get(pk=id_estudiante)
    except EstudianteM.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = EstudianteMForm(request.POST or None,request.FILES or None,instance=estudiante)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'cac/administracion/estudiantes/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_estudiantem', login_url=settings.LOGIN_URL)
def estudiantes_eliminar(request,id_estudiante):
    try:
        estudiante = Proyecto.objects.get(pk=id_estudiante)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    estudiante.delete()
    messages.success(request,'Se ha eliminado al estudiante correctamente')          
    return redirect('proyectos_index')

"""
    CRUD Proyectos
"""
@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.view_proyecto', login_url=settings.LOGIN_URL)
def proyectos_index(request):
    proyectos = Proyecto.objects.all()
    return render(request,'cac/administracion/proyectos/index.html',{'proyectos':proyectos})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.add_proyecto', login_url=settings.LOGIN_URL)
def proyectos_nuevo(request):
    formulario = ProyectoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'cac/administracion/proyectos/nuevo.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.change_proyecto', login_url=settings.LOGIN_URL)
def proyectos_editar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = ProyectoForm(request.POST or None,request.FILES or None,instance=proyecto)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'cac/administracion/proyectos/editar.html',{'formulario':formulario})

@login_required(login_url=settings.LOGIN_URL)
@permission_required('cac.delete_proyecto', login_url=settings.LOGIN_URL)
def proyectos_eliminar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el proyecto correctamente')          
    proyecto.delete()
    return redirect('proyectos_index')
    
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'lista_categorias'
    template_name= 'cac/administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']

class CategoriaView(View):
    form_class = CategoriaForm
    template_name = 'cac/administracion/categorias/nuevo.html'

    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'formulario':form})
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')
        return render(request,self.template_name,{'formulario':form})

"""
AUTENTICACION
"""
def cac_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            nxt = request.GET.get("next",None)
            messages.success(request, f' Bienvenido/a {username} !!')
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'cac/publica/login.html', {'form': form})

def cac_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'cac/publica/registrarse.html', {'form': form})

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def saludar(request,nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
        <p>Estoy haciendo mi primera prueba</p>
    """)

def ver_proyectos_2022_07(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_anio(request,anio):
    return HttpResponse(f"""
        <h1>Proyectos del  {anio}</h1>
        <p>Listado de proyectos</p>
    """)

def cursos_detalle(request,nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def cursos(request,nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)

# class CacLoginView(LoginView):
#     redirect_field_name = ''
#     template_name='cac/publica/login.html'