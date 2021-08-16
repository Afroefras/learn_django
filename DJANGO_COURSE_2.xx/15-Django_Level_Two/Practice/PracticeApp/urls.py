from os import name
from django.urls.conf import path
from PracticeApp import views

urlpatterns = [
    path('users', views.users, name='users'),
    path('', views.index, name='index'),
]