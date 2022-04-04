from django.db import models
from django.contrib.auth.models import UserManager
from authapp.models import User

# History
class SavedSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    marker = models.CharField('Партнёрский маркер', max_length=255, null=True, blank=True)
    host = models.CharField('Хост', max_length=255, null=True, blank=True)
    user_ip = models.CharField('IP пользователя', max_length=255, null=True, blank=True)
    locale = models.CharField('Локализация', max_length=255, null=True, blank=True)
    trip_class = models.CharField('Класс перелета', max_length=255, null=True, blank=True)
    adults = models.PositiveSmallIntegerField('Количество взрослых', null=True, blank=True, unique=True)
    children = models.PositiveSmallIntegerField('Количество детей', null=True, blank=True, unique=True)
    infants = models.PositiveSmallIntegerField('Количество младенцев', null=True, blank=True, unique=True)
    know_english = models.CharField('Знание английского языка', max_length=255, null=True, blank=True, unique=True)
    currency = models.CharField('Валюта', max_length=255, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = UserManager()

    class Meta:
        ordering = ['-add_time']
        verbose_name = "История поиска"
        verbose_name_plural = "Истории поиска"

    def __str__(self):
        return f'{self.user} {self.add_time}'

# Segment
class Segment(models.Model):
    user_request = models.ForeignKey(SavedSearch, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Запрос")
    travel_date = models.DateField(null=True, blank=True, verbose_name='Дата отправления')
    origin = models.CharField('IATA-код пункта отправления', max_length=255, null=True, blank=True)
    destination = models.CharField('IATA-пункта назначения', max_length=255, null=True, blank=True)

    objects = UserManager()

    class Meta:
        ordering = ['-travel_date']
        verbose_name = "Сегмент"
        verbose_name_plural = "Сегменты"

    def __str__(self):
        return f'{self.travel_date}'