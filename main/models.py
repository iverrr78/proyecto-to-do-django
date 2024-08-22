from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Creacion del modelo de tareas que se ocupa, slo contiene la 
#llave foranea del usuario y el titulo que es el nombre de la tarea
class Task(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
