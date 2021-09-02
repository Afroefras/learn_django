from django.db import models
from django.contrib.auth.models import User

class ModelUserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    url_LinkedIn = models.URLField(blank=True)
    image_ProfilePicture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self) -> str:
        return self.user.username