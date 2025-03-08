from django.db import models
from django.utils import timezone

class AppVarity(models.Model):
    APP_TYPE_CHOICE = [
        ('FD', 'FOOD'),
        ('PL', 'PLAY'),
        ('SG', 'SING'),
        ('MV', 'MOVIE')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)