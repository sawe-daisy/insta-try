from django.shortcuts import render, redirect
from .models import Image, Profile
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm,ProfileUpdateForm, UserUpdateForm, ImageUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        profForm=ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=profForm.save(commit=False)
            profile.user=user
            profile.save()

            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        profForm=ProfileForm()
    context={
        'form':form,
        'profForm': profForm
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        useForm=UserUpdateForm(request.POST, instance=request.user)
        profForm=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if useForm.is_valid() and profForm.is_valid():
            useForm.save()
            profForm.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('profile')
    
    else:
        useForm=UserUpdateForm(instance=request.user.profile)
        profForm=ProfileUpdateForm(instance=request.user.profile)

    context={
        'useForm':useForm,
        'profForm':profForm
    }

    return render(request, 'users/profile.html', context)

def index(request):
    context={
        'posts':Image.objects.all()
    }

    return render(request, 'index.html', context)
class PostListView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']


class PostDetailView(DetailView):
    model = Image
    template_name= 'posts/image_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image', 'caption', 'name']
    template_name='posts/postForm.html'
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['image', 'caption', 'name']
    template_name='posts/postForm.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'
    template_name= 'posts/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})