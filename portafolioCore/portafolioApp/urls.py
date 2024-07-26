from django.urls import path
from portafolioApp import views

urlpatterns = [
    path("",views.portafolio,name="portafolio")
]