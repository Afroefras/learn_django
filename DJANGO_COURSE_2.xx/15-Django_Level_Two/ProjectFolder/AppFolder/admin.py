from django.contrib import admin
from AppFolder.models import Topic, WebPage, AccessRecord

for model in [Topic, WebPage, AccessRecord]:
    admin.site.register(model)