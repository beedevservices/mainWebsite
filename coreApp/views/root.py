from django.shortcuts import render, redirect
from django.contrib import messages
from coreApp.models import *
from customerApp.models import *
from adminApp.models import *
from employeeApp.models import *

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }

def index(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'client_id' not in request.session:
        client = False
    else:
        client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee-id'])
    context = {
        'title': title,
        'client': client,
        'employee': employee
    }
    return render(request, 'index.html', context)

def about(request):
    title = {
        'title': 'About',
        'header': 'BeeDev Services',
    }
    if 'client_id' not in request.session:
        client = False
    else:
        client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee-id'])
    context = {
        'title': title,
        'client': client,
        'employee': employee
    }
    return render(request, 'about.html', context)

def projects(request):
    title = {
        'title': 'Past/Current Projects',
        'header': 'Our Work'
    }
    projects = Projects.objects.all().order_by('-lastUpdated').values  
    if 'client_id' not in request.session:
        client = False
    else:
        client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee-id'])
    context = {
        'title': title,
        'client': client,
        'employee': employee,
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def services(request):
    title = {
        'title': 'Services',
        'header': 'Our Services'
    }
    services = Service.objects.all().values()
    infos = Info.objects.all().values()
    if 'client_id' not in request.session:
        client = False
    else:
        client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee-id'])
    context = {
        'title': title,
        'client': client,
        'employee': employee,
        'services': services,
        'infos': infos,
    }
    return render(request, 'services.html', context)

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact Us'
    }
    if 'client_id' not in request.session:
        client = False
    else:
        client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee-id'])
    context = {
        'title': title,
        'client': client,
        'employee': employee,
    }
    return render(request, 'contact.html', context)


def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')