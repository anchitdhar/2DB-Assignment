from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=30, null=False, unique=True)
    

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
