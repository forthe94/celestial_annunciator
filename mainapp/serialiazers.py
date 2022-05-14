from rest_framework import serializers
from mainapp.models import SaveSearch
from authapp.models import User


# SaveSearch
class SaveSearchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(),
                                              required=False, allow_null=True)
    origin_location_code = serializers.CharField(max_length=64, required=False)
    destination_location_code = serializers.CharField(max_length=64, required=False)
    departureDate = serializers.DateField(required=False, format="%d.%m.%Y")
    returnDate = serializers.DateField(required=False, format="%d.%m.%Y")
    adults = serializers.IntegerField(required=False)
    children = serializers.IntegerField(required=False)
    travelClass = serializers.CharField(max_length=255, required=False)
    currency_code = serializers.CharField(max_length=64, required=False)
    includedAirlineCodes = serializers.CharField(max_length=64, required=False)
    nonStop = serializers.CharField(max_length=64, required=False)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")

    class Meta:
        model = SaveSearch
        fields = ['id', 'user', 'origin_location_code', 'destination_location_code', 'departureDate',
                  'returnDate', 'adults', 'children', 'travelClass', 'currency_code', 'includedAirlineCodes',
                  'nonStop', 'add_time']
