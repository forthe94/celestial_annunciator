from django.core.handlers import wsgi
from django.http import JsonResponse
from django.shortcuts import render

from common.travelpayouts_client import TravelPayoutsClient


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    if request.META['QUERY_STRING']:
        flights_data = search_flights(request)
        print(flights_data)
        return JsonResponse(flights_data, safe=False)

    return render(request, 'celestial_annucator/main.html', context)


def registration(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/registration.html', context)


def get_airports_by_term(request: wsgi.WSGIRequest):
    client = TravelPayoutsClient()
    term = request.GET['term']
    airports_data = client.get_airports_by_term(term)
    print(airports_data)
    return JsonResponse(airports_data, safe=False)


def search_flights(request):
    params = {
        'origin': request.GET['fromCity'],
        'destination': request.GET['toCity'],
        'departure_at': request.GET['dateStart'],
        'return_at': request.GET['dateBack'],
    }
    client = TravelPayoutsClient()
    data = client.prices_for_dates(**params)
    return data
