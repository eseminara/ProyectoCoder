from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def crea_curso (self,nombre,camada):

    curso = Curso (nombre=nombre, camada=camada)

    curso.save()

    return HttpResponse (f'Se creo el curso {curso.nombre} y la comision {curso.camada} ')
