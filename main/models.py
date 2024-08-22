from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
