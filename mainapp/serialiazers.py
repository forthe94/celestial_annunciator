from rest_framework import serializers
from mainapp.models import UserRequest, Segment
from authapp.models import User

# UserRequest
class UserRequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False, allow_null=True)
    marker = serializers.CharField(max_length=255, required=False)
    host = serializers.CharField(max_length=255, required=False)
    user_ip = serializers.CharField(max_length=255, required=False)
    locale = serializers.CharField(max_length=255, required=False)
    trip_class = serializers.CharField(max_length=255, required=False)
    adults = serializers.IntegerField(required=False)
    children = serializers.IntegerField(required=False)
    infants = serializers.IntegerField(required=False)
    know_english = serializers.CharField(max_length=255, required=False)
    currency = serializers.CharField(max_length=255, required=False)
    add_time = serializers.DateTimeField(required=False, format="%d.%m.%Y %H:%M")

    class Meta:
        model = UserRequest
        fields = ['id',
                    'user',
                    'marker',
                    'host',
                    'user_ip',
                    'locale',
                    'trip_class',
                    'adults',
                    'children',
                    'infants',
                    'know_english',
                    'currency',
                    'add_time'
                ]

# Segment
class SegmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_request = serializers.PrimaryKeyRelatedField(many=True, queryset=UserRequest.objects.all(), required=False, allow_null=True)
    travel_date = serializers.DateField(required=False, format="%Y-%m-%d")
    origin = serializers.CharField(max_length=255, required=False)
    destination = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Segment
        fields = ['id',
                    'user_request',
                    'travel_date',
                    'origin',
                    'destination',
                ]