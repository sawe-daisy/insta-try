from django.shortcuts import render
from .models import Image
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    post= Image.objects.all()

    return render(request, 'index.html', {"post":post})

def register(request):
    form= UserCreationForm()
    return render(request, 'users/register.html', {"form":form})
