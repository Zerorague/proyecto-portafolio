from django.urls import path
from aboutApp import views

urlpatterns = [
    path("",views.about, name ='about'),
]