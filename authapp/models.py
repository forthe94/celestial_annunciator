from django.contrib.auth.models import AbstractUser
from django.db import models

from authapp.manager import UserManager


# Create your models here.
class User(AbstractUser):

    email = models.EmailField('email address', unique=True, error_messages={
            'unique': "Данный адресс уже используется."})
    username = None
    age = models.PositiveIntegerField('Возраст', null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

