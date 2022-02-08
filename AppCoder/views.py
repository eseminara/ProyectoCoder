import email
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.form import CursoFormulario, CrearProfesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

# CRUD #

def busquedaCamada(request):
    
    return render (request, 'AppCoder/busquedaCamada.html')


def buscar(request):
    
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    
    #return HttpResponse (respuesta)


    if  request.GET["camada"]:

        respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada'] 
        cursos = Curso.objects.filter(camada__icontains=camada)

    #    return HttpResponse (respuesta)
        
        return render(request, "AppCoder/curso.html", {"cursos": cursos, "camada": camada})

    else: 
        
        return HttpResponse ('No envianste datos')

    #   #No olvidar from django.http import HttpResponse


def crea_curso (self,nombre,camada):

    curso = Curso (nombre=nombre, camada=camada)

    curso.save()

    return HttpResponse (f'Se creo el curso {curso.nombre} y la comision {curso.camada} ')


def cursoFormulario (request):
    
    if (request.method == 'POST'):
        
        miFormulario = CursoFormulario (request.POST) #Aca llega toda la info del html
        
        print (request.POST)
        
        if miFormulario.is_valid ():
            
            informacion = miFormulario.cleaned_data
        
            curso = Curso (nombre = informacion ['curso'], camada = informacion ['camada'])
        
            curso.save()
        
            return render (request, 'AppCoder/inicio.html')
        
        else:
            
            return HttpResponse ('Info no valida')
        
    else:
        
        miFormulario = CursoFormulario() #Form vacio para contruir el html
    
    return render (request, 'AppCoder/cursoFormulario.html', {'miFormulario': miFormulario})


def inicio (request):
    
    return render (request, 'AppCoder/inicio.html')


def curso (request):
    
    lista = Curso.objects.all()
    
    return render (request, 'AppCoder/curso.html', {'lista':lista})


def profesores (request):
    
    if (request.method == 'POST'): #Si consulto la data con un metodo Post
        
        formProfesor = CrearProfesor (request.POST) #Aca llega toda la info del html
        
        # print (request.POST)
        
        if formProfesor.is_valid ():
            
            infoprofesor = formProfesor.cleaned_data
        
            formProfesor = Profesor (nombre = infoprofesor ['nombre'], apellido = infoprofesor ['apellido'] , email = infoprofesor ['email'] , profesion = infoprofesor ['profesion'])
        
            formProfesor.save()
        
            return render (request, 'AppCoder/inicio.html')
        
        else:
            
            return HttpResponse ('Info no valida')
        
    else:
        
        formProfesor = CrearProfesor ()
    
    return render (request, 'AppCoder/profesores.html', {'formProfesor': formProfesor})


@login_required
def leer_profesores (request):
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores": profesores}
    
    return render (request, 'AppCoder/listaProfesores.html', contexto)


def eliminar_profesores (request, id_profesor):
    
    profesor = Profesor.objects.get(id = id_profesor)
    
    profesor.delete()
    
    profesor = Profesor.objects.all()

    return render (request, 'AppCoder/listaProfesores.html', {"profesores": profesor})


def editar_profesor (request, id_profesor):
    
    profesor = Profesor.objects.get(id = id_profesor)
    
    if (request.method == 'POST'):
        
        formProfesor = CrearProfesor (request.POST)
        
        print (formProfesor)
        
        if formProfesor.is_valid():
            
            informacion = formProfesor.cleaned_data
            
            profesor.nombre = informacion ['nombre']
            profesor.apellido = informacion ['apellido']
            profesor.email = informacion ['email']
            profesor.profesion = informacion ['profesion']

            profesor.save()
            
            return render (request, "AppCoder/inicio.html")
        
    else:
        
        formProfesor = CrearProfesor (initial = {'nombre' : profesor.nombre, 'apellido' : profesor.apellido, 'email' : profesor.email, 'profesion' : profesor.profesion})  
        
    return render (request, "AppCoder/editarProfesor.html", {"formProfesor" : formProfesor, "id_profesor" : id_profesor})
       
    
    
    


def estudiantes (request):
    
    return render (request, 'AppCoder/estudiantes.html')


def entregables (request):
    
    return render (request, 'AppCoder/entregables.html')



# CRUD - Clases Basadas en Vistas #

class CursoList (LoginRequiredMixin,ListView):
    model = Curso
    template_name = 'AppCoder/curso_list.html'
    
class CursoDetail (DetailView):
    model = Curso
    template_name = 'AppCoder/curso_detalle.html'
    
class CursoCreate (CreateView):
    model = Curso
    success_url = '/AppCoder/listaCurso'
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/curso_form.html'
    
class CursoUpdate (UpdateView):
    model = Curso
    success_url = '/AppCoder/listaCurso'
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/curso_form.html'
    
class CursoDelete (DeleteView):
    model = Curso
    success_url = '/AppCoder/listaCurso'
    template_name = 'AppCoder/curso_cofirm_delete.html'
    
    
# Loggin #

def login_request (request):
    
    if (request.method == 'POST'):
        
        form = AuthenticationForm (request, data = request.POST)
       
        if form.is_valid():
           
        #    usuario = form.cleaned_data.get ('username')     
        #    contra = form.cleaned_data.get ('password')
        #    user = authenticate (usuario = username, contra = password) 
        
            data = form.cleaned_data
           
            user = authenticate(username = data ['username'], password = data ['password'])
           
           
            if user is not None:
               
               login (request, user)
               
               return render (request, 'AppCoder/inicio.html',{'mensaje': f'Bienvenido {user.get_username()}'})
            
            else:
               
               return render (request, 'AppCoder/inicio.html',{'mensaje': 'Datos Invalidos'} )
           
        else:
            
            return render (request, 'AppCoder/inicio.html',{'mensaje': 'Formulario incorrecto' } )
                              
    
    else:
        form = AuthenticationForm()
        return render  (request, 'AppCoder/login.html', {'form': form})
        
        #return HttpResponse ('Bienvenidos al Loggin')
        

def register (request):
    
    if (request.method == 'POST'):
        
        form = UserCreationForm (request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            
            form.save()
    
        return render (request, 'AppCoder/inicio.html', {'mensaje': 'Usuario Creado'})
    
    else:
        
        form = UserCreationForm()
        
        return render (request,'AppCoder/register.html', {'form': form})


    




