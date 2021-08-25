from django.contrib import admin
from django.db import models
from app_model_forms.models import Users

for model in [Users]:
    admin.site.register(model)
