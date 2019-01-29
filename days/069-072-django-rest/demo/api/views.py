from rest_framework import generics

from quotes.models import Quote
from .serializers import QuoteSerializer
from .permissions import IsOwnerOrReadOnly


class QuoteList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all quotes in the DB.

    post:
    Create an awesome new quote.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return an individual quote.

    put:
    Update an existing quote.

    delete:
    Delete a single quote.
    """
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
