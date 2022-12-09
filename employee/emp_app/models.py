from django.db import models
from django.core.exceptions import ValidationError 

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name
    


class Role(models.Model):
    name=models.CharField(max_length=100,null=False)#,validators=[validate_name])

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"


    def clean(self):
        if not len(self.first_name)>0 or not len(self.last_name)>0:
            raise ValidationError("plesae enter value")
        
    
   
    

      