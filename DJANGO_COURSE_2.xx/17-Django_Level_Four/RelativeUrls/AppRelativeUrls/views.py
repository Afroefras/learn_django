from django.shortcuts import render

def index(request):
    return render(request, 'AppRelativeUrls/index.html')

def other(request):
    return render(request, 'AppRelativeUrls/other.html')

def rel_temp(request):
    return render(request, 'AppRelativeUrls/rel_temp.html')
