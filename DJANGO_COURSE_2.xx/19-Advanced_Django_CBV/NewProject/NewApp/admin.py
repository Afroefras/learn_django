from django.contrib import admin
from NewApp.models import School, Student

for model in [School, Student]:
    admin.site.register(model)
