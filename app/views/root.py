from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from ..models import *
import bcrypt

def index(request):
    data = {
        'Backend API': 'Running'
    }
    return JsonResponse(data)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

