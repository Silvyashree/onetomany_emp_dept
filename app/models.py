from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_No=models.IntegerField(primary_key=True)
    dept_location=models.CharField(max_length=100)

class Employee(models.Model):
    Employee_no=models.IntegerField(primary_key=True)
    Employee_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    Employee_email=models.EmailField(max_length=100)
    Employee_salary=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hiredate=models.DateField(auto_now=True)
    dept_name=models,models.ForeignKey("Department", on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    