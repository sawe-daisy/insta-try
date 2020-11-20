from django import forms
from .models import Profile

class RegistrationForm(forms.Form):
    username=forms.CharField(label= 'Username', max_length=20)
    bio= forms.CharField(label='Tell us about yourself', max_length=50)
    prof_pic=forms.ImageField(label='AVI')