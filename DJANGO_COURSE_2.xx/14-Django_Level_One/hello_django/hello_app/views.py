from django.shortcuts import render
from django.http import HttpResponse

def NewFunction(request):
    return HttpResponse('This is an example!')