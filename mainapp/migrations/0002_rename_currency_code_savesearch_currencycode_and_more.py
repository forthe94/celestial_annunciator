# Generated by Django 4.0 on 2022-05-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savesearch',
            old_name='currency_code',
            new_name='currencyCode',
        ),
        migrations.RenameField(
            model_name='savesearch',
            old_name='destination_location_code',
            new_name='destinationLocationCode',
        ),
        migrations.RenameField(
            model_name='savesearch',
            old_name='origin_location_code',
            new_name='originLocationCode',
        ),
    ]