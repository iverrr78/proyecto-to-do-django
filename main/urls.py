from django.urls import path
from .views import *

urlpatterns = [
    path("home", HomeView, name ="home"),
    #path("register", RegisterView, name = "register")
]