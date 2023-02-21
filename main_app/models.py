from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=1000)
    age = models.IntegerField()
    bio =  models.CharField(max_length=500)
    
    def __str__(self):
        return self.username

    def get_absolute_url(self): 
        return reverse('home')