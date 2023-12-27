from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    name=models.CharField(max_length=1000 )

class Message(models.Model):
    value=models.CharField(max_length=200000)
    date=models.DateTimeField(default=timezone.now, blank=True)
    room_name=models.CharField(max_length=2000)
    username=models.CharField(max_length=2000)

