from django.shortcuts import render, redirect
from django.contrib import messages

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }

def index(request):
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

def about(request):
    title = {
        'title': 'About',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'about.html', context)