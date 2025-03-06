from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_athlete = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to',
        related_name= 'custom_user_set',
        related_query_name='custom_user_set',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Unique related_name
        related_query_name='user',
    )

    def __str_(self):
        return self.username

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school_name = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Athlete: {self.first_name} {self.last_name}"


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)  # Name of the person managing the school account
    school_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    email  = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"School: {self.school_name}"
    
