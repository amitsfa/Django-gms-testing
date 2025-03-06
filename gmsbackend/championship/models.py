from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime

# Create your models here.

class sports(models.Model):
    SPORT_CHOICES =[
        ('Soccer','Soccer'),
        ('Basketball','Basketball'),
        ('Volleyball','Volleyball'),
    ]
    name = models.CharField(max_length=50, choices=SPORT_CHOICES)
    def __str__(self):
        return self.name

class championship(models.Model):
    name = models.CharField(max_length=50)
    sport = models.ManyToManyField(sports)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=50)
    def __str__(self):
        return self.name