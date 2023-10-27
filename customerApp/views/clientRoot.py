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
    context = {
        'title': title,
        'client': client,
    }
    return render(request, 'clientDash.html', context)

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