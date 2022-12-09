from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.

def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"all_emp.html",context)

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Employee Removed successfully")
        except:
            return HttpResponse("Enter valid Emp Id")

    emp_data=Employee.objects.all()
    context={
        'emp':emp_data
    }
    return render(request,"remove_emp.html",context)


def add_emp(request):
    if request.method=='POST':
        try:
            print(request.POST)
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            dept=int(request.POST.get('dept'))
            salary=request.POST.get('salary')
            bonus=request.POST.get('bonus')
            role=int(request.POST.get('role'))
            phone=request.POST.get('phone')
            #hire_date=request.POST['date']
            if dept==0 and role==0: 
                raise ValidationError("")
            emp_new=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
            emp_new.full_clean()
            emp_new.save()
            return HttpResponse("Employee Added Succesfully")
           # return redirect("/")
        except ValidationError:
            #messages.info(request,"Please enter valid value")
            return HttpResponse('Please Enter valid value to form')
       # print("yes")
    else:
        dept_data=Department.objects.all()
        role_data=Role.objects.all()
        context={
            'dept_data':dept_data,
            'role_data':role_data,
            'add_update':'add'
        }
     
        return render(request,"add_emp.html",context)

def update_emp(request,id=0):
    #update_id=id
    if request.method=='POST':
        try:
            print(request.POST)
            emp=Employee.objects.get(id=id)
            emp.first_name=request.POST.get('first_name')
            emp.last_name=request.POST.get('last_name')
            emp.dept_id=int(request.POST.get('dept'))
            emp.salary=request.POST.get('salary')
            emp.bonus=request.POST.get('bonus')
            emp.role_id=int(request.POST.get('role'))
            emp.phone=request.POST.get('phone')
            #hire_date=request.POST['date']
            if emp.dept==0 and emp.role==0: 
                raise ValidationError("")
            #emp_new=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
            emp.full_clean()
            emp.save()
            return HttpResponse("Employee Updated Succesfully")
           # return redirect("/")
        except ValidationError:
            #messages.info(request,"Please enter valid value")
            return HttpResponse('Please Enter valid value to form')
       
        
    else:
        if id:
            emp=Employee.objects.get(id=id)
            dept_data=Department.objects.all()
            role_data=Role.objects.all()
            #update_id=id
            context={
                'dept_data':dept_data,
                'role_data':role_data,
                'update_emp':emp,
                'display_id':id
            }
            return render(request,'update_emp.html',context)
        else:
            emp=Employee.objects.all()
            context={
                'emp_data':emp,
                'display_id':id
            }
            return render(request,"update_emp.html",context)

    

def filter_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role').lower()
        emp=Employee.objects.all()
        if name:
            emps=emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emp.filter(dept__dept_name__icontains=dept)
        if role:
            emps=emp.filter(role__name__icontains=role)

        context={
            'emps':emps
        }
        return render(request,"all_emp.html",context)
    else:
        return render(request,"filter_emp.html")