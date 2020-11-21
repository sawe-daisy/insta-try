from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    bio= models.CharField(max_length=100)
    username=models.CharField(max_length=20)
    email= models.EmailField()
    prof_pic= CloudinaryField('image', blank=True)

    def __str__(self):
        return self.username

class Image(models.Model):
    image= CloudinaryField('image')
    author= models.ForeignKey(Profile, on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    caption= models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name