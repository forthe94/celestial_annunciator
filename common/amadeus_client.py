# API Client for Amadeus
# https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference

from amadeus import Client, ResponseError
from celestial_annucator import settings


class AmadeusClient(Client):
    def __init__(self):
        super().__init__(client_id=settings.AMADEUS_API_KEY, client_secret=settings.AMADEUS_SECRET_KEY)


