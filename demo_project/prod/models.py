from django.db import models

# Task Model
class Task(models.Model):
    task_number = models.IntegerField(
        null=False,
        verbose_name='Task Number',
    )
    task_title = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Task Title'
    ) 
    task_description = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Task Description'
    ) 
    task_planned_date = models.DateField(
        auto_now=False,
        blank=True,
        null=True,
        auto_now_add=False,
        verbose_name='Task Planned Date'
    )
    task_start_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name='Task Start Date'
    )
    task_due_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name='Task Due Date'
    )
    task_finish_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name='Task Finish Date'
    )

    task_team  = models.ManyToManyField(
        'rh.Employee',
        through='TaskByEmployee',
        through_fields=('task', 'employee'),
    )
    
    def __str__(self):
        return f'{self.task_title}'

class TaskByEmployee(models.Model):
    task = models.ForeignKey(
        'Task',
        null = True,
        blank=True,
        on_delete=models.SET_NULL)
    employee = models.ForeignKey(
        'rh.Employee',
        null = True,
        blank=True,
        on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'Task by Employee'
        verbose_name_plural = 'Tasks by Employees'

    def __str__(self):
        pass
