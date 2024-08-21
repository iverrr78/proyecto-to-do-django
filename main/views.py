from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def HomeView(request):
    print("hola mundo!")
    if request.method == "POST":
        return redirect('tasks')
    return render(request, "main/home.html", {})

def TasksView(request):
    form = UserForm()
    return render(request, "main/register.html", {'form': form})