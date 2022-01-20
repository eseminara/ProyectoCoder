from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def crea_curso (self,nombre,camada):

    curso = Curso (nombre=nombre, camada=camada)

    curso.save()

    return HttpResponse (f'Se creo el curso {curso.nombre} y la comision {curso.camada} ')


def inicio (request):
    
    return render (request, 'AppCoder/inicio.html')


def curso (request):
    
    lista = Curso.objects.all()
    
    return render (request, 'AppCoder/curso.html', {'lista':lista})


def profesores (request):
    
    return render (request, 'AppCoder/profesores.html')


def estudiantes (request):
    
    return render (request, 'AppCoder/estudiantes.html')


def entregables (request):
    
    return render (request, 'AppCoder/entregables.html')


