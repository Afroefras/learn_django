from typing import Pattern


from django.urls.conf import path
from template_app import views

urlpatterns = [
    path('', views.index, name='index')
]