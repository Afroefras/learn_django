from django.shortcuts import render
from NewApp.models import User

def index(request):
    return render(request, 'templates_NewApp/index.html', context={'insert_h2':'Please go to /users'})

def users(request):
    all_users = User.objects.order_by('email')
    return render(request, 'templates_NewApp/users.html', context={'users':all_users})