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

def index(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'url' not in request.session:
        url = '/'
        request.session['url'] = url
        prev_url = '/'
        request.session['prev_url'] = prev_url
    else:
        prev_url = request.session['url']
        url = '/'
        request.session['url'] = url
        request.session['prev_url']= prev_url
    cart = request.session['cart']
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
        'cart': cart,
        'url': url,
        'prev_url': prev_url
    }
    return render(request, 'index.html', context)

def about(request):
    title = {
        'title': 'About',
        'header': 'BeeDev Services',
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/about/'
    request.session = url
    cart = request.session['cart']
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
        'cart': cart,
        'url': url,
        'prev_url': prev_url
    }
    return render(request, 'about.html', context)

def projects(request):
    title = {
        'title': 'Past/Current Projects',
        'header': 'Our Work'
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/projects/'
    request.session['url'] = url
    cart = request.session['cart']
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
        'cart': cart,
        'url': url,
    }
    return render(request, 'projects.html', context)

def services(request):
    title = {
        'title': 'Services',
        'header': 'Our Services'
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/services/'
    request.session['url'] = url
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
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
        'cart': cart,
        'url': url,
    }
    return render(request, 'services.html', context)

def addToCart(request):
    url = request.session['url']
    service = request.POST.get('service_id')
    remove = request.POST.get('remove')
    add = request.POST.get('add')
    cart = request.session.get('cart')
    thePrice = request.POST.get('price')
    item = Service.objects.get(id=request.POST.get('service_id'))
    # if + is clicked
    if add:
        plus = cart.get(str(item.id))['quantity']
        plus = plus + 1
        if cart.get(str(item.id))['price'] != 'None':
            price = int(cart.get(str(item.id))['price'])
            total = int(cart.get(str(item.id))['total'])
            total = price * plus
        else:
            total = 'TBD'
        cart[str(service)]['total'] = total
        cart[str(service)]['quantity'] = plus
    # if - is clicked
    elif remove:
        min = cart.get(str(item.id))['quantity']
        price = int(cart.get(str(item.id))['price'])
        total = int(cart.get(str(item.id))['total'])
        if min <= 1:
            cart.pop(service)
        else:
            min = min - 1
            total = price * min
            cart[str(service)]['quantity'] = min
            cart[str(service)]['total'] = total
    # if item not in cart and add to cart is clicked
    else:
        # if cart is empty
        if cart == {}:
            # set item, quantity, price and total to item clicked or default
            item = cart.get(str(item.id), {})
            quantity = item.get('quantity', 0)
            price = (item.get('price', thePrice))
            total = item.get('total', 0)
            item['quantity'] = quantity + 1
            item['price'] = price
            total = item['price']
            item['total'] = total
            # adds item['quantity'], item['price'], item['total'] to the cart 
            cart[str(service)] = item
        else:
            item = cart.get(str(item.id), {})
            quantity = item.get('quantity', 0)
            price = (item.get('price', thePrice))
            total = item.get('total', 0)
            item['quantity'] = quantity + 1
            item['price'] = price
            total = item['price']
            item['total'] = total
            # adds item['quantity'], item['price'], item['total'] to the cart 
            cart[str(service)] = item
    request.session['cart'] = cart
    return redirect(f'{url}')

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact Us'
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/contact/'
    request.session['url'] = url
    cart = request.session['cart']
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
        'cart': cart,
        'url': url,
        'prev_url': prev_url,
    }
    return render(request, 'contact.html', context)

def cart(request):
    title = {
        'title': 'The Cart',
        'header': 'Cart',
    }
    prev_url = request.session['url']
    request.session['prev_url'] = prev_url
    url = '/cart/'
    request.session['url'] = url
    cart = request.session['cart']
    if cart == {}:
        services = False
    else:
        ids = list(request.session.get('cart').keys())
        services = Service.objects.filter(id__in=ids)
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
        'cart': cart,
        'url': url,
        'prev_url': prev_url,
        'services': services,
    }
    # print('what is services', services)
    return render(request, 'cart.html', context)


def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')