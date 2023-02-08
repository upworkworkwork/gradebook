from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Subject

# Create your views here.
def index(request):           
    year3 = Subject.objects.all()[12:13] # current semester/year retrived from database 
    sub = Subject.objects.all()[12:16] # 06 subjects of current yeaer  
    seme4 = Subject.objects.all()[12:13]
    return render(request, 'index.html', {'sub': sub, 'year3': year3, 'seme4': seme4})

def semesterone(request):
  year1 = Subject.objects.all()[1:2]
  subj = Subject.objects.all()[0:4]
  seme1 = Subject.objects.all()[0:1]
  return render(request, 'autumn2021.html', {'year1': year1, 'subj':subj, 'seme1':seme1})

def semestertwo(request):
    year2 = Subject.objects.all()[4:5]
    sub = Subject.objects.all()[4:8]
    seme2 = Subject.objects.all()[4:5]
    return render(request, 'spring2022.html', {'year2': year2, 'sub':sub, 'seme2':seme2})

def semesterthree(request):
    year2 = Subject.objects.all()[8:9]
    subj = Subject.objects.all()[8:12]
    seme3 = Subject.objects.all()[8:9]
    return render(request, 'autumn2022.html', {'year2': year2, 'subj':subj, 'seme3':seme3})

def semesterfive(request):
  year3 = Subject.objects.all()[16:17]
  subj = Subject.objects.all()[16:20]
  seme5 = Subject.objects.all()[16:17]
  return render(request, 'autumn2023.html', {'year3': year3, 'subj':subj, 'seme5':seme5})

def semestersix(request):
  year4 = Subject.objects.all()[20:21]
  subjj = Subject.objects.all()[20:24]
  seme6 = Subject.objects.all()[20:22]
  return render(request, 'spring2024.html', {'year4': year4, 'subjj':subjj, 'seme6':seme6})
#testing = '<h1>testing... testing... testingss. </h1>'
     #HttpResponse(testing)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else: 
                user = User.objects.create_user(username= username, email=email, password=password)    
                user.save();
                return redirect('login')
        else: 
            messages.info(request, 'password not the same')
            return redirect('register')
    else:                    
        return render(request, 'register.html')
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None: 
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:     
       return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
