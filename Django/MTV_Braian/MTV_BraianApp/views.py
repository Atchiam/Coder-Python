from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "index.html",{}) #return render(request, "nombre del HTML",{Argumentos o contexto "lo que se modifica o entra en el HTML"})

