from django.contrib import admin
from aboutApp import models

# Register your models here.

class FormacionAdmin(admin.ModelAdmin):
    list_display = ["carrera","institucion","ingreso","egreso","descripcion"]
    readonly_fields = ["created","updated"]

class HabilidadAdmin(admin.ModelAdmin):
    list_display = ["nombre","nivel","imagen"]

class NivelAdmin(admin.ModelAdmin):
    list_display = ["nivel",]

class TrabajoAdmin(admin.ModelAdmin):
    list_display = ["titulo","empresa","ingreso","egreso"]

admin.site.register(models.Formacion,FormacionAdmin)
admin.site.register(models.Habilidad,HabilidadAdmin)
admin.site.register(models.Nivel,NivelAdmin)
admin.site.register(models.Trabajo,TrabajoAdmin)


