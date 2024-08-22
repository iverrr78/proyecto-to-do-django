from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeView(request):
    print("hola mundo!")
    if request.method == "POST":
        return redirect('register')
    return render(request, "main/home.html", {})

def TasksView(request):
    if request.user.is_authenticated:
        print("usuario: ", request.user)
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.userid = request.user  # Asignar el usuario actual
                task.save()
                return redirect('tasks')  # Redirige a la misma vista para evitar reenvío de formulario
        else:
            form = TaskForm()

        tasks = Task.objects.filter(userid=request.user)

        return render(request, 'main/tasks.html', {
            'task_form': form,
            'tasks': tasks
        })
    else:
        return redirect('login')

def deletetask(request, taskid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            task = get_object_or_404(Task, id=taskid, userid=request.user)
            task.delete()
            return redirect('tasks')
    else:
        return redirect('login')