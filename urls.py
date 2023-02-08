from django.urls import path
from .models import Subject
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('semesterone', views.semesterone, name='semesterone'),
    path('semestertwo', views.semestertwo, name='semestertwo'),
    path('semesterthree', views.semesterthree, name='semesterthree'),
    path('semesterfive', views.semesterfive, name='semesterfive'),
    path('semestersix', views.semestersix, name='semestersix'),
   
] 