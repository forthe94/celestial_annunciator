from datetime import date

from common.travelpayouts_client import TravelPayoutsClient


def test_prices_for_dates():
    client = TravelPayoutsClient()
    ret = client.prices_for_dates(
        origin='MOW',
        destination='CMB',
        departure_at='2022-04'
    )
    print(ret)
    assert ret['success'] == True
