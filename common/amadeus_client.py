# API Client for Amadeus
# https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference

from amadeus import Client, ResponseError
from celestial_annucator import settings


class AmadeusClient(Client):
    def __init__(self):
        super().__init__(client_id=settings.AMADEUS_API_KEY, client_secret=settings.AMADEUS_SECRET_KEY)


if __name__ == '__main__':

    client = Client(client_id='jtwPsO2MVYam4ph7QJ65GbK9jZQSerMe', client_secret='caYb6K7dRcZysXhe')
    try:
        response = client.shopping.flight_offers_search.get(
            originLocationCode='MOW',
            destinationLocationCode='MRV',
            departureDate='2022-04-17',
            adults=1,
            currencyCode='RUB'
        )
        print(response.data)
    except ResponseError as error:
        print(error)

