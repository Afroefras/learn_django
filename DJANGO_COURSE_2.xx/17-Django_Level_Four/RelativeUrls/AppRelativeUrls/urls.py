from django.urls.conf import path
from AppRelativeUrls import views

app_name = 'to_app'

urlpatterns = [
    path('rel_temp', views.rel_temp, name='rel_temp'),
    path('other', views.other, name='other'),
]