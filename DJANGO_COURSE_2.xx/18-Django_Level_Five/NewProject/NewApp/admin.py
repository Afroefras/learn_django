from django.contrib import admin
from django.db import models
from NewApp.models import ModelUserProfile

for model in [ModelUserProfile,]:
    admin.site.register(model)