from rest_framework import serializers

from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('quote', 'author', 'source', 'cover', 'user')
