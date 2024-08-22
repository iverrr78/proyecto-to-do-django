from django.shortcuts import render, redirect
from .forms import *
from .models import *
import random

# Create your views here.

def HomeView(request):
    print("hola mundo!")
    if request.method == "POST":
        return redirect('register')
    return render(request, "main/home.html", {})

def RegisterView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data["username"]
            Email = form.cleaned_data["email"]
            Password = form.cleaned_data["password"]
            Userid = random.randint(1, 100000000)
            user = User(userid = Userid, username = Username, email = Email, password = Password)
            user.save()
            return redirect()
    else:
        form = UserForm()
        return render(request, "main/register.html", {'form': form})