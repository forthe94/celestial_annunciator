import json
import pathlib

import pytest

from celestial_annucator.cities_data import load_airports_data


@pytest.fixture
def resources():
    return pathlib.Path(__file__).parent / 'resources'


@pytest.fixture
def airports_starts_with_data(resources):
    return json.loads((resources / 'airports_starts_with.json').read_text('utf-8'))


@pytest.fixture
def airports_data():
    load_airports_data()

