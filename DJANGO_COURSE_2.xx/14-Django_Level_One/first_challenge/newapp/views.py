from django.shortcuts import render
from django.http import HttpResponse

def challenge(request):
    return HttpResponse('<h1>Challenge completed!</h1>')