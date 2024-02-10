from django.shortcuts import render, redirect
from django.contrib import messages
from customerApp.models import *

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }
def clientPortal(request):
    title = {
        'title': 'Client',
        'header': 'BeeDev Services',
    }
    if 'client_id' not in request.session:
        return redirect('/client/logReg')
    client = Customer.objects.get(id=request.session['client_id'])
    if 'employee_id' in request.session:
        return redirect('/employee/')
    employee = False
    context = {
        'title': title,
        'client': client,
        'employee': employee
    }
    print('what is context:', context)
    return render(request, 'clientDash.html', context)

# def clientLogReg(request):
#     title = {
#         'title': "Client Portal",
#         'header': 'Client Portal - BeeDev Services'
#     }
#     prev_url = request.session['url']
#     request.session['prev_url'] = prev_url
#     url = '/client/logReg/'
#     request.session['url'] = url
#     if 'employee_id' not in request.session

def clientLogReg(request):
    title = {
        'title': "Client Portal",
        'header': 'Client Portal - BeeDev Services'
    }
    if 'employee_id' in request.session:
        request.session['employee_id'] = False
    if 'client_id' not in request.session:
        context = {
            'title': title,
        }
        return render(request, 'clientLogReg.html', context)