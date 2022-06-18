from django.shortcuts import render
from .models import *

# Create your views here.

def inicio (request):
    return render (request, "desafioApp\main.html", {} )

def cursos (request):
    cursos = Curso.objects.all()
    ctx={'cursos':cursos}
    return render (request, "desafioApp\cursos.html", ctx  )

def eventos (request):
    eventos = Evento.objects.all()
    ctx1={'eventos':eventos}
    return render (request, "desafioApp\eventos.html", ctx1  )