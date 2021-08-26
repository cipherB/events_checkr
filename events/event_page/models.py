from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('homepage')
    
    
