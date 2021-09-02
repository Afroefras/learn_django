from django.urls.conf import path
from PracticeApp import views

app_name = 'go_to'

urlpatterns = [
    path('kenobi', views.kenobi, name='kenobi'),
    path('general', views.general, name='general'),
]
