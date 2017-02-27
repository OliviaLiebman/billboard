from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=50, null=True, default='Author')
    title = models.CharField(max_length=200, null=True, default='title')
    text = models.CharField(max_length=1000, null=True, default='text')

    created_date = models.DateTimeField(
        default = timezone.now)

    def __str__(self):
        return self.title


