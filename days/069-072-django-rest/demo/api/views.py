from rest_framework import generics
from .serializers import QuoteSerializer

from quotes.models import Quote


class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
