from django.contrib import admin

# Import My models
from .models import Employee
from .models import EmployeeStatus
from .models import BankAccount

class EmployeeAdmin(admin.ModelAdmin):
    # readonly_fields = ('salary',)
    list_display = ('fname', 'lname', 'status')
    list_filter = ('status',)


# Register my models.
admin.site.register(EmployeeStatus)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(BankAccount)


