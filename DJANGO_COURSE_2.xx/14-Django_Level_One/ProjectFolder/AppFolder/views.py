from django.shortcuts import render

def index(request):
    return render(request,'AppFolder/index.html',context={'insert_this':"I'm in views.py"})
