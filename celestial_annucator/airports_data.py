import requests
from celestial_annucator import settings

airports_data = None


def load_airports_data():
    global airports_data
    resp = requests.get(settings.AIRPORTS_DATA_URL)
    print(resp)
    if resp.status_code != 200:
        raise Exception('Failed to load airports data')
    airports_data = resp.json()
    print(airports_data)


def get_data():
    if airports_data is None:
        raise Exception('Airports data not loaded')
    return airports_data
