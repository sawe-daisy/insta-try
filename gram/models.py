from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio= models.CharField(max_length=100)
    prof_pic= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        
        img=Image.open(self.prof_pic.path)
        if img.height >300 or img.height > 300:
            output_size= (300, 300)
            img.thumbnail(output_size)
            img.save(self.prof_pic.path)


class Image(models.Model):
    image= CloudinaryField('image')
    author= models.ForeignKey(Profile, on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    caption= models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name