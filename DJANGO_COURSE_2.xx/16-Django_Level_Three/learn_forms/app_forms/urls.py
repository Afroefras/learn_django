from django.urls.conf import path
from app_forms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage', views.formpage, name='formpage'),
]