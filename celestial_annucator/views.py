from django.core.handlers import wsgi
from django.http import JsonResponse
from django.shortcuts import render
from common.amadeus_client import AmadeusClient, ResponseError
from common.travelpayouts_client import TravelPayoutsClient


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    return render(request, 'celestial_annucator/main.html', context)


def registration(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/registration.html', context)


def get_airports_by_term(request: wsgi.WSGIRequest):
    client = TravelPayoutsClient()
    term = request.GET['term']
    airports_data = client.get_airports_by_term(term)
    return JsonResponse(airports_data, safe=False)


def flights_search(request: wsgi.WSGIRequest):
    request_params = request.GET
    flights_result = {}
    params = {
        'originLocationCode': request_params['fromCity'],
        'destinationLocationCode': request_params['toCity'],
        'departureDate': request_params['dateStart'],
        'adults': 1,
        'currencyCode': 'RUB'
    }
    client = AmadeusClient()
    try:
        response = client.shopping.flight_offers_search.get(**params)
        flights_result['one_way'] = {'data': response.result['data'],
                                     'dictionaries': response.result['dictionaries']}

    except ResponseError as error:
        print(error)
    if 'dateBack' in request_params:
        params = {
            'originLocationCode': request_params['toCity'],
            'destinationLocationCode': request_params['fromCity'],
            'departureDate': request_params['dateBack'],
            'adults': 1,
            'currencyCode': 'RUB'
        }
        client = AmadeusClient()
        try:
            response = client.shopping.flight_offers_search.get(**params)
            flights_result['two_way'] = {'data': response.result['data'],
                                         'dictionaries': response.result['dictionaries']}
        except ResponseError as error:
            print(error)
    return JsonResponse(flights_result, safe=False)
