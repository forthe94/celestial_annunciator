from rest_framework import serializers
from mainapp.models import SaveSearch
from authapp.models import User


# SaveSearch
class SaveSearchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    originLocationCode = serializers.CharField(max_length=64, required=False)
    destinationLocationCode = serializers.CharField(max_length=64, required=False)
    departureDate = serializers.DateField(required=False, format="%d.%m.%Y")
    returnDate = serializers.DateField(required=False, format="%d.%m.%Y")
    adults = serializers.IntegerField(required=False)
    children = serializers.IntegerField(required=False)
    infants = serializers.IntegerField(required=False)
    travelClass = serializers.CharField(max_length=255, required=False)
    currencyCode = serializers.CharField(max_length=64, required=False)
    validatingAirlineCodes = serializers.CharField(max_length=64, required=False)
    nonStop = serializers.CharField(max_length=64, required=False)
    total = serializers.DecimalField(max_digits=19, decimal_places=2)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")
    route = serializers.JSONField()

    class Meta:
        model = SaveSearch
        fields = ['id', 'user', 'origin_location_code', 'destination_location_code', 'departureDate',
                  'returnDate', 'adults', 'children', 'infants', 'travelClass', 'currency_code',
                  'validatingAirlineCodes', 'nonStop', 'total', 'add_time', 'route']
