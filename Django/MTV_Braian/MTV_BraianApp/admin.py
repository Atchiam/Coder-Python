from django.contrib import admin

from MTV_BraianApp.models import Familia

# Register your models here.
#Atchiam - ladesiempre96

class FamiliaAdmin(admin.ModelAdmin):  
    list_display = ("nombre","apellido","edad","fecha_de_creacion","profeccion","parentesco")
admin.site.register (Familia, FamiliaAdmin)
