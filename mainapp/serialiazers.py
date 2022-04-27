from rest_framework import serializers
from mainapp.models import SaveSearch
from authapp.models import User

# SaveSearch
class SaveSearchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False, allow_null=True)
    origin_location_code = serializers.CharField(max_length=255, required=False)
    destination_location_code = serializers.CharField(max_length=255, required=False)
    departure_date = serializers.DateField(required=False, format="%d.%m.%Y")
    adults = serializers.IntegerField(required=False)
    currency_code = serializers.CharField(max_length=255, required=False)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")

    class Meta:
        model = SaveSearch
        fields = ['id', 'user', 'origin_location_code', 'destination_location_code', 'departure_date', 'adults',
                  'currency_code', 'add_time']