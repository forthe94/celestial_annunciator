import dataclasses
import requests
from celestial_annucator import settings


@dataclasses.dataclass
class TravelPayoutsClient:
    token: str = settings.TRAVELPAYOUTS_API_TOKEN
    base_url: str = settings.TRAVELPAYOUTS_API_URL

    def _base_request(
            self,
            method: str,
            url: str,
            headers: dict = None,
            params: dict = None,
            body: dict = None
    ):
        url = self.base_url + url

        if not params:
            params = {}
        params['token'] = self.token

        res = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=body
        )
        return res

    def prices_for_dates(
            self,
            origin: str,
            destination: str,
            departure_at: str,
            return_at: str = None,
            direct: bool = False,
            limit: int = 30,
            page: int = 1,
            sorting: str = 'price',
            unique: bool = False
    ):
        params = {
            'origin': origin,
            'destination': destination,
            'departure_at': departure_at,
            'return_at': return_at,
            'direct': 'true' if direct else 'false',
            'limit': limit,
            'page': page,
            'sorting': sorting,
            'unique': 'true' if unique else 'false'
        }
        ret = self._base_request(
            'GET',
            'prices_for_dates',
            params=params
        )

        return ret.json()
