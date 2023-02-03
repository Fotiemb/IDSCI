from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=10)


class Data(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    telephone = models.CharField(max_length=10, default='')

