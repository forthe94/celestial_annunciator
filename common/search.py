from django.http import JsonResponse
from common.amadeus_client import AmadeusClient, ResponseError


def get_search(params):
    client = AmadeusClient()
    try:
        response = client.shopping.flight_offers_search.get(**params)
    except ResponseError as error:
        print(error)
    return JsonResponse(response.result, safe=False)
