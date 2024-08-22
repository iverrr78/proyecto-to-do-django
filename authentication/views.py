from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.

def RegisterView(request):
    if request.method == "POST":
        print("buxade")
        form = RegisterUserForm(request.POST)
        form.save()
        return redirect("home")
    else:
        form = RegisterUserForm()
        return render(request, "authentication/register.html", {"form":form} )
