from django.urls.conf import path
from NewApp import views

urlpatterns = [
    path('users', views.users, name='users'),
    path('', views.index, name='index'),
]