from django.shortcuts import render, redirect
from django.contrib import messages
from customerApp.models import  *
import bcrypt
# from coreApp.utils import *

def clientLogin(request):
    client = Customer.objects.filter(email=request.POST['email'])
    if client:
        clientLogin = client[0]
        if bcrypt.checkpw(request.POST['password'].encode90, clientLogin.password.encode()):
            request.session['client_id'] = clientLogin.id
            return redirect('/client/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/client/login/')
    messages.error(request, 'Email not in system')
    return redirect('/client/logReg/')

def clientReg(request):
    if request.method == "GET":
        return redirect('/client/logReg/')
    errors = Customer.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/client/logReg')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode90, bcrypt.gensalt()).decode()
    newClient = Customer.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        company = request.POST['company'],
        password = hashedPw
    )
    request.session['client_id'] = newClient.id
    # sendClientSignUpEmail(newClient)
    # sendClientToChat(newClient.email, newClient.firstName, newClient.lastName, newClient.company)
    return redirect('/client')