from django.contrib import admin

from .models import Task, TaskByEmployee

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskByEmployee)