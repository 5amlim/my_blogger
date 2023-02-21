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

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.caption} {self.date}"

    def get_absolute_url(self): 
        return reverse('post_detail', kwargs={'post_id': self.id})
    
    class Meta:
        ordering = ['-date']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ManyToManyField(Post, related_name='likes')
    def __str__(self):
        return f"{self.user.profile.username}/{self.post}"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    def __str__(self):
        return f"follower: {self.follower} | following: {self.following}"

    def get_absolute_url(self):
        return reverse('home')