from django.urls.conf import path
from NewApp import views

app_name = 'NewApp'

urlpatterns = [
    path('register', views.register, name='register'),
]