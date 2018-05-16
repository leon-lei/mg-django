from django.db import models
from django.contrib.auth.models import User


class Tribe(models.Model):
    tribe_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tribe_image', blank=True)

class Event(models.Model):
    tribe = models.ForeignKey(Tribe, on_delete=models.DO_NOTHING)