import requests
from celestial_annucator import settings

airlines_data = None


def load_airlines_data():
    global airlines_data
    resp = requests.get(settings.CITIES_DATA_URL)

    if resp.status_code != 200:
        raise Exception('Failed to load airports data')

    airlines_data = resp.json()


def get_data():
    if airlines_data is None:
        raise Exception('Airports data not loaded')
    return airlines_data