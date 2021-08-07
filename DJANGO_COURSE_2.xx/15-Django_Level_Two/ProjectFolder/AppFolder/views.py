from django.shortcuts import render
from AppFolder.models import Topic, WebPage, AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    return render(request, 'template_AppFolder/index.html', context={'webpages':webpages_list})
