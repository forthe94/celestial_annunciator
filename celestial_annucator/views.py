from django.core.handlers import wsgi
from django.http import JsonResponse
from django.shortcuts import render

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
    params = {
        'origin': request_params['fromCity'],
        'destination': request_params['toCity'],
        'departure_at': request_params['dateStart'],
        'return_at': request_params.get('dateBack'),
    }
    client = TravelPayoutsClient()
    flights_data = client.prices_for_dates(**params)
    print(flights_data)
    return JsonResponse(flights_data, safe=False)
