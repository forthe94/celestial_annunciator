import requests
from celestial_annucator import settings

cities_data = None


def load_cities_data():
    global cities_data
    resp = requests.get(settings.CITIES_DATA_URL)

    if resp.status_code != 200:
        raise Exception('Failed to load airports data')

    cities_data = resp.json()


def get_data():
    if cities_data is None:
        raise Exception('Airports data not loaded')
    return cities_data
