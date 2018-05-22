from django.db import models
from accounts.models import UserProfile

class Tribe(models.Model):
    tribe_name = models.CharField(max_length=250)
    chieftain = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tribe_image', blank=True)

    def __str__(self):
        return self.tribe_name

    class Meta:
        ordering = ('tribe_name',)

class Event(models.Model):
    event_name = models.CharField(max_length=250, blank=True)
    event_date = models.DateField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='event_image', blank=True)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ('event_date',)