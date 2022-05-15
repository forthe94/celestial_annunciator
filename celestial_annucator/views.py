from django.http import JsonResponse
from django.shortcuts import render
from common.travelpayouts_client import TravelPayoutsClient
from common.search import get_search


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    return render(request, 'celestial_annucator/main.html', context)


def registration(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/registration.html', context)

def get_airports_by_term(request):
    client = TravelPayoutsClient()
    term = request.GET['term']
    airports_data = client.get_airports_by_term(term)
    return JsonResponse(airports_data, safe=False)


def flights_search(request):
    request_params = request.GET
    params = {x: request_params.get(x) for x in request_params.keys()}
    params['currencyCode'] = 'RUB'
    return get_search(params)