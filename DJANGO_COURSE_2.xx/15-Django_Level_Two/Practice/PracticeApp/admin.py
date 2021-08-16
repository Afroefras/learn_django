from django.contrib import admin
from django.db import models
from PracticeApp.models import Students_Practice

for model in [Students_Practice,]:
    admin.site.register(model)
