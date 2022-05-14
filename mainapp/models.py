from django.db import models
from authapp.models import User


# DB logs
class DBLog(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10)
    message = models.TextField()
    filename = models.CharField(max_length=255)
    func_name = models.CharField(max_length=255)
    lineno = models.CharField(max_length=255)


    class Meta:
        ordering = ['-time']
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return f'{self.message}'


# History
class SaveSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    origin_location_code = models.CharField('originLocationCode', max_length=64)
    destination_location_code = models.CharField('destinationLocationCode', max_length=64)
    departureDate = models.DateField('departureDate')
    returnDate = models.DateField('returnDate')
    adults = models.PositiveSmallIntegerField('adults', default=1)
    children = models.PositiveSmallIntegerField('children')
    travelClass = models.CharField('travelClass', max_length=255)
    currency_code = models.CharField('currencyCode', max_length=64, default='RUB')
    includedAirlineCodes = models.CharField('includedAirlineCodes', max_length=64)
    nonStop = models.CharField('nonStop', max_length=64, default=False)
    add_time = models.DateTimeField('add_time', auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering = ['-add_time']
        verbose_name = "История поиска"
        verbose_name_plural = "Истории поиска"

    def __str__(self):
        return f'{self.user} {self.add_time}'
