from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.CharField(primary_key = True, max_length=50)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)

class TaskList(models.Model):
    tasklistid = models.CharField(primary_key = True, max_length = 50)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models

TASK_IMPORTANCE_CHOICES = [
    ('Alto', 'Alto'),
    ('Medio', 'Medio'),
    ('Bajo', 'Bajo')
]

TASK_STAGE_CHOICES= [
    ('En proceso', 'En proceso'),
    ('Finalizado', 'Finalizado'),
    ('Sin iniciar', 'Sin iniciar')
]
class Task(models.Model):
    taskid = models.CharField(primary_key = True, max_length=50)
    tasklistid = models.ForeignKey(TaskList, on_delete= models.CASCADE)
    importance = models.CharField(max_length=20, choices=TASK_IMPORTANCE_CHOICES)
    stage = models.CharField(max_length=20, choices= TASK_STAGE_CHOICES)
    title = models.CharField(max_length= 50)
    description = models.TextField()
