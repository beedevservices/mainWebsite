from django.shortcuts import render, redirect
from django.contrib import messages

# title = {
#     'title': '',
#     'header': 'BeeDev Services',
# }
def clientDash(request):
    title = {
        'title': 'Client',
        'header': 'BeeDev Services',
    }
    if 'user_id' not in request.session:
        user = False
    context = {
        'title': title,
        'user': user,
    }
    return render(request, 'clientDash.html', context)