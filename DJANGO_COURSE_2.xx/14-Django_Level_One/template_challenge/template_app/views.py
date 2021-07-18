from django.shortcuts import render

def index(request):
    return render(request,'template_app/index.html',context={'help_me':'Help me, please!'})
