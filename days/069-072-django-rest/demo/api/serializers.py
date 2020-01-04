from rest_framework import serializers

from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    # This is not included in the videos. Without this setting, it was possible
    # to set the user value to something other than the currently logged-in
    # user. This setting hides the user field from the form in the API frontend
    # and sets the currently logged-in users as the field value by default.
    # See also: https://stackoverflow.com/a/53193276
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Quote
        fields = ('quote', 'author', 'source', 'cover', 'user')
