from django.shortcuts import render, redirect
from .models import Image
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    post= Image.objects.all()

    return render(request, 'index.html', {"post":post})

def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Successfully created Account for {username}!')
            return redirect('gram-landing')
    else:
        form= UserCreationForm()
    return render(request, 'users/register.html', {"form":form})
