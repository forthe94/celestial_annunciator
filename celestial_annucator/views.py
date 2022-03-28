from django.shortcuts import render


def index(request):
    context = {'title': 'FlyScanner - поиск авиабилетов'}
    return render(request, 'celestial_annucator/main.html', context)
