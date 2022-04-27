from django.apps import AppConfig

from celestial_annucator.cities_data import load_cities_data
from celestial_annucator.airports_data import load_airports_data
from celestial_annucator.airlines_data import load_airlines_data


class MyAppConfig(AppConfig):
    name = 'celestial_annucator'

    def ready(self):
        load_cities_data()
        load_airports_data()
        load_airlines_data()
