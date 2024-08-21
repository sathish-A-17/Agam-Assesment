from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    accounts = (
        ('user','User'),
        ('admim', 'Admin')
    )

    role = models.CharField(max_length=10,choices=accounts,default='user')

    def __str__(self):
        return self.username