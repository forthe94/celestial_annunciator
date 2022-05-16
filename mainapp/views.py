import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from authapp.models import User
from mainapp.models import SaveSearch
from mainapp.serialiazers import SaveSearchSerializer


class SaveSearchViewSet(viewsets.ModelViewSet):
    queryset = SaveSearch.objects.all()
    serializer_class = SaveSearchSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]

@csrf_exempt
def save_search(request):
    if request.method == 'POST':
        current_user = request.user
        if current_user.is_authenticated:
            json_data = json.loads(request.body)
            adults = json_data.get('adults')
            children = json_data.get('children')
            departure_date = json_data.get('departureDate')
            if departure_date:
                departure_date = datetime.strptime(departure_date, '%Y-%m-%d')
                print(departure_date)
            destination_location_code = json_data.get('destinationLocationCode')
            returnDate = json_data.get('returnDate')
            if returnDate:
                returnDate = datetime.strptime(returnDate, '%Y-%m-%d')
            infants = json_data.get('infants')
            travelClass = json_data.get('travelClass')
            currency_code = 'RUB'
            validatingAirlineCodes = json_data.get('validatingAirlineCodes')
            nonStop = json_data.get('nonStop')
            total = json_data.get('total')
            route = json_data.get('route')
            if route:
                route = json.dumps(route, indent=4)
            exist_user = User.objects.filter(pk=current_user.pk).last()
            SaveSearch.objects.create(
                user=exist_user,
                adults=adults,
                children=children,
                departureDate=departure_date,
                destination_location_code=destination_location_code,
                returnDate=returnDate,
                infants=infants,
                travelClass=travelClass,
                currency_code=currency_code,
                validatingAirlineCodes=validatingAirlineCodes,
                nonStop=nonStop,
                total=total,
                route=route
            )
            return JsonResponse({'auth': True}, safe=False)
        else:
            return JsonResponse({'auth': False}, safe=False)