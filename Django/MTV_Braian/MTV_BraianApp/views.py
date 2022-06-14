from django.http import HttpRequest
from django.shortcuts import render

from MTV_BraianApp.models import Familia

# Create your views here.

def inicio(request):
    return render(request, "index.html",{}) #return render(request, "nombre del HTML",{Argumentos o contexto "lo que se modifica o entra en el HTML"})

def familia(request):
    familias = Familia.objects.all()
    
    ctx = {"familias": familias}
    
    return render (request, "famila.html", ctx)