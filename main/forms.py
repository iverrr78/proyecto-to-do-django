from django import forms
from .models import Task

#Creacion del fomulario que sirve para crear nuevas tareas
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title'] 