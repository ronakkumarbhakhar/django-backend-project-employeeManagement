from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    base_salary = models.PositiveIntegerField()
    job_type = models.CharField(max_length=300)
    address = models.TextField(max_length=1000)
    contact_no = models.PositiveBigIntegerField()
    employer_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name

class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    employer_id = models.ForeignKey(User,on_delete=models.CASCADE)


class Salary(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    month =models.CharField(max_length=25)
    paid = models.BooleanField(default=False)
    # reciept = models.ImageField()
    employer_id = models.ForeignKey(User,on_delete=models.CASCADE)

