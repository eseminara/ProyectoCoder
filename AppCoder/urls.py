from django.urls import path
from AppCoder import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('', views.inicio, name='inicio'),
    path ('crea-curso/<nombre>/<camada>/', views.crea_curso),
    path ('curso/', views.curso, name='cursos'),
    path ('profesores/', views.profesores, name='profesores'),
    path ('estudiantes/' , views.estudiantes, name='estudiantes'),
    path ('entregables/' , views.entregables, name = 'entregables'),
    path ('cursoFormulario/' , views.cursoFormulario, name = 'cursoFormulario'),
    path ('busquedaCamada/' , views.busquedaCamada, name = 'BusquedaFormulario'),
    path ('buscar/' , views.buscar, name = 'Buscar'),
    path ('listaProfesores/' , views.leer_profesores, name = 'ListaProfesores'),
    path ('eliminarProfesor/<id_profesor>' , views.eliminar_profesores, name = 'EliminarProfesor'),
    path ('editarProfesor/<id_profesor>', views.editar_profesor, name = 'EditarProfesor'),

# PATH CRUD VISTA BASADO EN CLASE #
    
    path ('listaCurso/', views.CursoList.as_view(), name='List'),
    path ('detalleCurso/<pk>', views.CursoDetail.as_view(), name='Detail'),
    path ('actualizaCurso/<pk>', views.CursoUpdate.as_view(), name='Edit'),
    path ('crearCurso/', views.CursoCreate.as_view(), name='Create'),
    path ('eliminarCurso/<pk>', views.CursoDelete.as_view(), name='Delete'),
   
# LOGIN /  REGISTER / LOGOUT #
    path ('login/', views.login_request, name='Login'),
    path ('register/', views.register, name='Register'),
    path ('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),


    
    
    
    
]   