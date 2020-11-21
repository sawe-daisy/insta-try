from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    bio= forms.CharField(label='Tell us about yourself', max_length=50)
    prof_pic=forms.ImageField(label='AVI')
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2', 'bio', 
        'prof_pic']

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label = "Image:")
    name = forms.CharField(label = "Image Name:", max_length=50)
    caption = forms.CharField(label = "Image Caption:", max_length=300)
    