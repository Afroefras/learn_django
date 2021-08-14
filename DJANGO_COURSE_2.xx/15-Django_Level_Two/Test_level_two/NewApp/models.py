from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}: {self.email}'
