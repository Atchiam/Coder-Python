from django.db import models


#Create your models here.
class Familia (models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    edad = models.IntegerField ()
    fecha_de_creacion= models.DateTimeField(auto_now_add=True)
    profeccion = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)

