from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from mainapp.models import SaveSearch
from mainapp.serialiazers import SaveSearchSerializer


class SaveSearchViewSet(viewsets.ModelViewSet):
    queryset = SaveSearch.objects.all()
    serializer_class = SaveSearchSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]

