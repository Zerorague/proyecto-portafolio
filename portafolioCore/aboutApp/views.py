from django.shortcuts import render
from aboutApp import models

# Create your views here.
def about(request):
    formaciones = models.Formacion.objects.all()
    trabajos = models.Trabajo.objects.all()
    habilidades = models.Habilidad.objects.all()

    context = {
        "formaciones":formaciones,
        "trabajos":trabajos,
        "habilidades":habilidades,
    }
    return render(request,"about.html",context)