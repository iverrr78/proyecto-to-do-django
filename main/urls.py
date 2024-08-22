from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView, name ="home"),
    path("tasks", TasksView, name="tasks"),
    path('tasks/delete/<int:taskid>/', deletetask, name='deletetask'),
    #path("register", RegisterView, name = "register")
]