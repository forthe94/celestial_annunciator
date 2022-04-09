import requests
import settings

airports_data = None


def load_airports_data():
    global airports_data
    resp = requests.get(settings.AIRPORTS_DATA_URL)
    if resp.status_code != 200:
        raise Exception('Failed to load airports data')
    airports_data = resp.json()


def get_data():
    if airports_data is None:
        raise Exception('Airports data not loaded')
    return airports_data
