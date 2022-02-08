from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class CursoFormulario (forms.Form):
    
    curso = forms.CharField()
    camada = forms.IntegerField()
    
    
class CrearProfesor (forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    profesion= forms.CharField()
    
class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField()