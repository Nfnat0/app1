from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    no = models.IntegerField()
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return f'{self.no}:{self.text} '
