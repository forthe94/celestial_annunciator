from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from mainapp.models import SavedSearch, Segment
from mainapp.serialiazers import UserRequestSerializer, SegmentSerializer


class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = SavedSearch.objects.all()
    serializer_class = UserRequestSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]

class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]


def history(request):
    return render(request, 'celestial_annucator/main.html')
