from django.shortcuts import render
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.

def RegisterView(request):
    form = RegisterUserForm
    return render(request, "authentication/register.html", {"form":form} )
