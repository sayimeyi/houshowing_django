from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'houshowing/login.html')

def login(request):
    username = request.POST.get('loginUsername')
    password = request.POST.get('loginPassword')
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponseRedirect('/houshowing/home')
    else:
        return HttpResponseRedirect('/houshowing')




def registerPage(request):
    return render(request, 'houshowing/register.html')

def register(request):
    username = request.POST.get('registerUsername')
    email = request.POST.get('registerEmail')
    password = request.POST.get('registerPassword')
    user = User.objects.create_superuser(username, email, password)
    user.save()
    return render(request, 'houshowing/login.html')

def home(request):
    return render(request, 'houshowing/index.html')