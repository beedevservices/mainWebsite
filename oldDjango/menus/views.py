from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *

def mIndex(request):
    return render(request, 'mIndex.html')

def tabMenus(request):
    return render(request, 'tabMenus.html')

def hiddenMenus(request):
    return render(request, 'hiddenMenus.html')

def sidebarMenus(request):
    return render(request, 'sidebarMenus.html')

def stickyMenus(request):
    return render(request, 'stickyMenus.html')

def dropdowns(request):
    return render(request, 'dropdowns.html')