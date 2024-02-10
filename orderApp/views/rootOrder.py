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
# prev_url = request.session['url']
# request.session['prev_url'] = prev_url
# url = '/about/'
# request.session = url
# cart = request.session['cart']
# if 'client_id' not in request.session:
#     client = False
# else:
#     client = Customer.objects.get(id=request.session['client_id'])
# if 'employee_id' not in request.session:
#     employee = False
# else:
#     employee = Employee.objects.get(id=request.session['employee-id'])
# context = {
#     'title': title,
#     'client': client,
#     'employee': employee,
#     'cart': cart,
#     'url': url,
#     'prev_url': prev_url
# }

def orderRequest(request):
    title = {
        'title': 'Order Request',
        'header': 'Order Request',
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/order/request/'
    request.session = url
    # cart = request.session['cart']
    if 'employee_id' not in request.session:
        employee = False
    else:
        employee = Employee.objects.get(id=request.session['employee_id'])
    if 'client_id' not in request.session:
        client = False
        messages.error(request, 'Please create an account to finish sending your order request')
        return redirect('/client/logReg/')
    else:
        client = Customer.objects.get(id=request.session['client_id'])
        context = {
            'title': title,
            'client': client,
            'employee': employee,
            'url': url,
            'prev_url': prev_url,
            # 'cart': cart,
        }
        return render(request, 'confirm.html', context)