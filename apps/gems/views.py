from rest_framework import viewsets
from .models import GemListing
from .serializers import GemListingSerializer


class GemListingViewSet(viewsets.ModelViewSet):
    queryset = GemListing.objects.all()
    serializer_class = GemListingSerializer
