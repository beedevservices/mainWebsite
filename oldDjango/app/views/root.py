from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from ..models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

