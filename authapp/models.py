from django.contrib.auth.models import AbstractUser
from django.db import models
from authapp.manager import UserManager


# Create your models here.
class User(AbstractUser):
    # username = None
    email = models.EmailField('email address', unique=True, error_messages={
            'unique': "A user with that email already exists."})
    age = models.PositiveIntegerField('Возраст', null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

