from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField('Возраст', null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
