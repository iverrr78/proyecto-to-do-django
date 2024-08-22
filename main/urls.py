from django.urls import path
from .views import *

#Urls que se utilizan en la aplicacion
urlpatterns = [
    #url de la pagina principal
    path("", HomeView, name ="home"),
    #url de la pagina donse se pueden ver y crear tareas
    path("tasks", TasksView, name="tasks"),
    #url para borrar las tareas
    path('tasks/delete/<int:taskid>/', deletetask, name='deletetask'),
]