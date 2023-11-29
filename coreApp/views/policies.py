from django.shortcuts import render, redirect
from django.contrib import messages

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }

def termsOfUse(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    pass

def cookies(request):
    title = {
        'title': 'Cookie Use',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'cookie.html', context)

def disclaimer(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'index.html', context)

def linking(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'index.html', context)

def privacy(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'index.html', context)

def refund(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'index.html', context)

def jobs(request):
    title = {
        'title': 'Home',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'index.html', context) 