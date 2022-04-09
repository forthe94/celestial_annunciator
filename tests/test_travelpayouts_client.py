import json
from datetime import date

from common.travelpayouts_client import TravelPayoutsClient
from tests.conftest import airports_starts_with_data, airports_data


def test_prices_for_dates():
    client = TravelPayoutsClient()
    ret = client.prices_for_dates(
        origin='MOW',
        destination='CMB',
        departure_at='2022-04'
    )
    assert ret['success'] is True


def test_aiports_by_term(airports_starts_with_data, airports_data):
    client = TravelPayoutsClient()

    queued_ports = client.get_airports_by_term('й')

    assert queued_ports == airports_starts_with_data
