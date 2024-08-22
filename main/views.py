from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista que sirve para retornar la plantilla html de la pagina principal
def HomeView(request):
    if request.method == "POST":
        return redirect('register')
    return render(request, "main/home.html", {})

#Vista que sirve para retornar la plantilla html de la pagina que contiene
#Las tareas y tambien maneja el comportamiento del formulario para crear
#tareas
def TasksView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.userid = request.user
                task.save()
                return redirect('tasks')
        else:
            form = TaskForm()

        tasks = Task.objects.filter(userid=request.user)

        return render(request, 'main/tasks.html', {
            'task_form': form,
            'tasks': tasks
        })
    else:
        return redirect('login')

#Vista que sirve para manejar el comportamiento del formulario que permite
#borrar tareas
def deletetask(request, taskid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            task = get_object_or_404(Task, id=taskid, userid=request.user)
            task.delete()
            return redirect('tasks')
    else:
        return redirect('login')