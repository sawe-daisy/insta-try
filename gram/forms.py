from django import forms
from .models import Profile

class RegistrationForm(forms.Form):
    username=forms.CharField(label= 'Username', max_length=20)
    bio= forms.CharField(label='Tell us about yourself', max_length=50)
    prof_pic=forms.ImageField(label='AVI')

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label = "Image:")
    name = forms.CharField(label = "Image Name:", max_length=50)
    caption = forms.CharField(label = "Image Caption:", max_length=300)
    