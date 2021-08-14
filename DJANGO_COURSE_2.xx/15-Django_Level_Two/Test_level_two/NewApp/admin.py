from django.contrib import admin
from django.contrib import admin
from NewApp.models import User

for model in [User,]:
    admin.site.register(model)