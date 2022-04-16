# API Client for TravelPayouts
# https://support.travelpayouts.com/hc/en-us/articles/203956163

import dataclasses
from itertools import islice

import requests
from celestial_annucator import settings, cities_data


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
        """
        @param origin: - IATA код аэропорта вылета например 'MOW'
        @param destination: - IATA код аэропорта прилета например 'CMB'
        @param departure_at: - дата вылета в формате ISO 'YYYY-MM' или 'YYYY-MM-DD'
        @param return_at: - дата прилёта в формате ISO 'YYYY-MM' или 'YYYY-MM-DD',
            для билетов в один конец указывать не обязательно
        @param direct: - флаг без пересадок
        @param limit: - количество билетов на странице
        @param page: - номер страницы
        @param sorting: - сортировка 'price' или 'route'
        @param unique: - флаг только уникальные маршруты
        @return:
        """
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

    @staticmethod
    def get_airports_by_term(term: str):
        ap_data = cities_data.get_data()

        def airports_by_term_generator(data: dict, term_str: str):
            for airport in data:
                if airport['name'] and airport['name'].lower().startswith(term_str.lower()):
                    yield airport

        return list(islice(airports_by_term_generator(ap_data, term), settings.AIRPORTS_BY_TERM_COUNT))
