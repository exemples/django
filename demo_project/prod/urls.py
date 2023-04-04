from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='prod-index'),
    path('tasks', views.TaskListView.as_view(), name='prod-all-tasks'),
    path('tasks', views.tasks, name='prod-all-tasks'),
    path('tasks/<int:id>', views.tasksByEmpl, name='prod-tasks-by-empl'),
    path('task/<int:id>', views.taskById, name='prod-task-by-id'),
    path('form/', views.taskForm, name='prod-task-form'),
]
