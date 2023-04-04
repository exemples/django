from django.db import models

# Employee Model
class Employee(models.Model):
    """Model definition for Employee."""
    # TODO: Define fields here
    code = models.CharField(max_length=50)
    fname = models.CharField(
        max_length=50, 
        verbose_name='First Name',
        null=False
    ) 
    lname = models.CharField(
        max_length=50, 
        verbose_name='Last Name',
        null=False
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )
    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Salary',
        null=False    
    )
    
    valide = models.BooleanField(
        default=True
    )

    status = models.ForeignKey(
        'EmployeeStatus', 
        max_length=50,
        null=True,
        default='Active',
        verbose_name='Status',
        on_delete=models.SET_NULL,
        related_name='employees')
    
    tasks = models.ManyToManyField('prod.Task')

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of Employee."""
        return f'{self.fname}, {self.lname}'



class EmployeeStatus(models.Model):
    """Model definition for EmployeeStatus."""

    # TODO: Define fields here
    status = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Status',
        choices=[
            ('Active','Active'),
            ('Fired', 'Fired'),
            ('Quit', 'Quit'),
            ('Retired', 'Retired')
        ]
    )
    class Meta:
        """Meta definition for EmployeeStatus."""

        verbose_name = 'Employee Status'
        verbose_name_plural = 'Employees Status'

    def __str__(self):
        """Unicode representation of EmployeeStatus."""
        return f'{self.status}'


# BankAcount Model
class BankAccount(models.Model):
    account_number = models.CharField(
        max_length=50
    )
    bank_name = models.CharField(   
        max_length=50
    )
    bank_account_holder = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='bank_account',
    )

    class Meta:
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'

    def __str__(self):
        return f'{self.bank_name}:{self.account_number}'

