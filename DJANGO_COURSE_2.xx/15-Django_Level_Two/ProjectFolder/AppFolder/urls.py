from django.urls.conf import path
from AppFolder import views

urlpatterns = [
    path('', views.index, name='index'),
]