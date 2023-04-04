from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView, TemplateView

from .models import Task

# Home Views
def index(request):
    return render(request, 'prod/index.html')


# Task List Views
def tasks(request):
    return render(request, 'prod/tasks.html')

class TaskListView(ListView):
    template_name = "prod/tasks.html"
    model = Task
    context_object_name = 'tasks'

# Task Detail Views
def tasksByEmpl(request, id):
    return render(request, 'prod/tasks_by_empl.html')

def taskById(request, id):
    return render(request, 'prod/task_by_id.html')

# New Task Views
def taskForm(request):
    return render(request, 'prod/task_form.html')



