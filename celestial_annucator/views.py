from django.shortcuts import render


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    return render(request, 'celestial_annucator/main.html', context)

def login(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/login.html', context)

def registration(request):
    context = {'title': 'FlyScanner - Вход'}
    return render(request, 'celestial_annucator/registration.html', context)