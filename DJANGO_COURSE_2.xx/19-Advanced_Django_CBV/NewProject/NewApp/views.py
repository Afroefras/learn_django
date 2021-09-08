from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

def index(request):
    return render(request, 'NewApp/index.html')

class NewView(TemplateView):
    template_name = 'NewApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert_h2'] = 'Home page'
        return context

class ListView_School(ListView):
    context_object_name = 'schools' # by default, it creates a lower-case+"_list" list-object --> school_list
    model = models.School

class DetailView_School(DetailView):
    context_object_name = 'school_detail' # by default, it creates a lower-case list-object --> school
    model = models.School
    template_name = "NewApp/school_detail.html"
