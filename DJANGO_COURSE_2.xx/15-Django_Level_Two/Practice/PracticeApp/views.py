from django.shortcuts import render
from PracticeApp.models import Students_Practice

def index(request):
    return render(request, 'templates_PracticeApp/index.html', context={'insert_h2':'Please go to /users'})


def users(request):
    all_students = Students_Practice.objects.order_by('age')
    return render(request, 'templates_PracticeApp/users.html', context={'all_students':all_students})