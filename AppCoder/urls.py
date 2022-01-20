from django.urls import path
from AppCoder import views


urlpatterns = [
    path ('', views.inicio, name='inicio'),
    path ('crea-curso/<nombre>/<camada>', views.crea_curso),
    path ('curso', views.curso, name='cursos'),
    path ('profesores', views.profesores, name='profesores'),
    path ('estudiantes' , views.estudiantes, name='estudiantes'),
    path ('entregables' , views.entregables, name = 'entregables'),

    

    
]