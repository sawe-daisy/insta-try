from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image= CloudinaryField('image')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    caption= models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)



