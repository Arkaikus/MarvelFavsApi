from django.db import models
from django.contrib.auth.models import User


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comicId = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    thumbnail = models.URLField()
    description = models.TextField(default="")
