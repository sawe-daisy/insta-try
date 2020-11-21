from django.shortcuts import render, redirect
from .models import Image
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    post= Image.objects.all()

    return render(request, 'index.html', {"post":post})

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'users/register.html', {"form":form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
