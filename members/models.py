from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    thumb=models.ImageField(upload_to = "media/" )
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    link=models.CharField(max_length=100)