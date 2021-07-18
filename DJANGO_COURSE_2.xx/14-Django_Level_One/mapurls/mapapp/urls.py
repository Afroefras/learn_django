from django.urls.conf import path
from mapapp import views

urlpatterns = [
    path('',views.mapped)
]