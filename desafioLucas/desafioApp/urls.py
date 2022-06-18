from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("cursos",cursos, name="cursos"),
    path("eventos",eventos, name= "eventos")
]
