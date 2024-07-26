from django.shortcuts import render
from portafolioApp.models import Project

# Create your views here.

def portafolio(request):
    proyectos = Project.objects.all()
    context = {"proyectos":proyectos,}

    return render(request,"portafolio.html",context)