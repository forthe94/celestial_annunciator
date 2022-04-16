import json
from pprint import pprint

from django.core.handlers import wsgi
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from celestial_annucator import cities_data, airports_data, airlines_data
from common.amadeus_client import AmadeusClient, ResponseError
from common.travelpayouts_client import TravelPayoutsClient


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    return render(request, 'celestial_annucator/main.html', context)


def registration(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/registration.html', context)


@api_view(['GET'])
def get_airports_by_term(request):
    term = request.query_params.get('term')
    client = TravelPayoutsClient()
    airports_data = client.get_airports_by_term(term)
    return JsonResponse(airports_data, safe=False)


def process_moscow_airports_and_another(arrival_city_code, arrival_code, departure_city_code, departure_code,
                                        arrival_name, departure_name):

    if arrival_city_code == "'MOW'" and arrival_code == "'DME'":
        arrival_name = [name for name in arrival_name if name == "'Домодедво'"]
    elif arrival_city_code == "'MOW'" and arrival_code == "'VKO'":
        arrival_name = [name for name in arrival_name if name == "'Внуково'"]
    elif arrival_city_code == "'MOW'" and arrival_code == "'SVO'":
        arrival_name = [name for name in arrival_name if name == "'Шереметьево'"]

    if departure_city_code == "'MOW'" and departure_code == "'DME'":
        departure_name = [name for name in departure_name if name == "'Домодедво'"]
    elif departure_city_code == "'MOW'" and departure_code == "'VKO'":
        departure_name = [name for name in departure_name if name == "'Внуково'"]
    elif departure_city_code == "'MOW'" and departure_code == "'SVO'":
        departure_name = [name for name in departure_name if name == "'Шереметьево'"]

    if len(arrival_name) > 0:
        arrival_result = arrival_name[0]
    else:
        arrival_result = arrival_city_code

    if len(departure_name) > 0:
        departure_result = departure_name[0]
    else:
        departure_result = departure_city_code

    return arrival_result, departure_result


def segments_process(segments, locations, airports_config, airlines_config):
    for segment in segments:
        arrival = segment['arrival']
        arrival_code = arrival['iataCode']
        departure = segment['departure']
        departure_code = departure['iataCode']
        arrival_city_code = locations[arrival_code]['cityCode']
        departure_city_code = locations[departure_code]['cityCode']
        arrival_name = [airport['name'] for airport in airports_config if airport['city_code'] == arrival_city_code]
        departure_name = [airport['name'] for airport in airports_config if airport['city_code'] == departure_city_code]
        result = process_moscow_airports_and_another(arrival_city_code, arrival_code, departure_city_code,
                                                     departure_code, arrival_name, departure_name)
        segment['arrival'].update({'airportName': result[0]})
        segment['departure'].update({'airportName': result[1]})

        airline_code = f'{segment["operating"]["carrierCode"]}'
        airline_name = [airline['name'] for airline in airlines_config if airline['code'] == airline_code]
        if len(airline_name) > 0:
            airline_name = airline_name[0]
        else:
            airline_name = airline_code
        segment["operating"].update({'airlineName': airline_name})
    return segments


@api_view(['GET'])
def flights_search(request):
    params = {
        'originLocationCode': request.query_params.get('fromCity'),
        'destinationLocationCode': request.query_params.get('toCity'),
        'departureDate': request.query_params.get('dateStart'),
        'adults': 1,
        'currencyCode': 'RUB'
    }
    client = AmadeusClient()
    try:
        response = client.shopping.flight_offers_search.get(**params)
        if response.status_code == 200:
            result = response.result
            locations = result['dictionaries']['locations']

            data = result['data']
            for route in data:
                itineraries = route.get('itineraries')
                for itinerary in itineraries:
                    segments = itinerary['segments']
                    airports_config = airports_data.get_data()
                    airlines_config = airlines_data.get_data()
                    segments_process(segments, locations, airports_config, airlines_config)

        else:
            result = []
    except ResponseError as error:
        pprint(error)
        result = []
    pprint(result)
    return JsonResponse(result, safe=False)
