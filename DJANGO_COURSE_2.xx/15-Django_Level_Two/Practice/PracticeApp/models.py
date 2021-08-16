from django.db import models

class Students_Practice(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()
    fav_topic = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}: {self.age} years old'