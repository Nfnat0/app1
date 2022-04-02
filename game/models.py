from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.TextField()
    src = models.TextField()

    def __str__(self):
        return f'{self.id}:{self.word}'
