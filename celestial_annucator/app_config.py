from django.apps import AppConfig

from celestial_annucator.airports_data import load_airports_data


class MyAppConfig(AppConfig):
    name = 'celestial_annucator'

    def ready(self):
        load_airports_data()
