from django.db import models

# Create your models here.
# company model
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# employee model 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField('Device', through='Checkout')

    def __str__(self):
        return self.name


# device model
class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

# checkout model
class Checkout(models.Model):
    CONDITION_CHOICES = [
        ('G', 'Good'),
        ('F', 'Fair'),
        ('P', 'Poor'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('CHECKED_OUT', 'Checked Out'),
        ('RETURNED', 'Returned')
    ])
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES)

    def __str__(self):
        return f'{self.device.name} checked out to {self.employee.name}'
