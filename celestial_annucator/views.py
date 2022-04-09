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
    term = request.GET['fromCity']
    airports_data = client.get_airports_by_term(term)
    return JsonResponse(airports_data, safe=False)
