from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Human(models.Model):
    desc=models.CharField(max_length=50,null=True,default=None)
    time=models.DateField(auto_now_add=True)