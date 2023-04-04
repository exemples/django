from django.shortcuts import render

from .forms import EmployeeForm

from .models import Employee
from django.db.models import Avg

# Create your views here.

def index(request):
    return render(request, 'rh/index.html')


def emplList(request):
    employees = Employee.objects.all().order_by('-salary')
    employees_count = employees.count
    average_salary = employees.aggregate(Avg('salary'))
    return render(request, 'rh/empl_list.html', {
        'employees':employees,
        'employee_count': employees_count,
        'average_salary': average_salary,
        })


def emplDetail(request, id):
    employee = Employee.objects.get(pk=id)
    return render(request, 'rh/empl_detail.html', {'employee':employee})


def emplForm(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    else:
        form = EmployeeForm()
    return render(request, 'rh/empl_form.html', context={'form':form})
