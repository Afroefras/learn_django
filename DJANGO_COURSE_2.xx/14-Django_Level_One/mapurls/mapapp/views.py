from django.http.response import HttpResponse
from django.shortcuts import render

def mapped(request):
    return HttpResponse('<h1><em>This is a mapped object</em></h1>')
