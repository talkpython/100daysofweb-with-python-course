from django.forms import ModelForm

from .models import Quote


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        exclude = ('user',)
