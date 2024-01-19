from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    addresh=models.TextField()
    profile_pic=models.ImageField()