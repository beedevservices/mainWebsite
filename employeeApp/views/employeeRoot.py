from django.shortcuts import render, redirect
from django.contrib import messages
from employeeApp.models import *

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }

def employeePortal(request):
    title = {
        'title': 'Employee',
        'header': 'BeeDev Services'
    }
    if 'employee_id' not in request.session:
        return redirect('/employee/logReg/')
    employee = Employee.objects.get(id=request.session['employee_id'])
    if 'client_id' in request.session:
        return redirect('/client/')
    client = False
    context = {
        'title': title,
        'client': client,
        'employee': employee
    }
    return render(request, 'employeeDash.html', context)

def employeeLogReg(request):
    title = {
        'title': "Employee Portal",
        'header': 'Employee Portal - BeeDev Services'
    }
    if 'client_id' in request.session:
        request.session['client_id'] = False
    if 'employee_id' not in request.session:
        context = {
            'title': title,
        }
        return render(request, 'clientLogReg.html', context)