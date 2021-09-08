from django.urls.conf import path, re_path
from . import views

app_name = 'NewApp'

urlpatterns = [
    path('', views.ListView_School.as_view(), name='list'),
    re_path('(?P<pk>[-\w]+)/', views.DetailView_School.as_view(), name='detail'),
]