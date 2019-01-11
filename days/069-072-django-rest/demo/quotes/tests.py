from django.test import TestCase
from django.urls import reverse

from quotes.forms import QuoteForm
from quotes.models import Quote

QUOTES = [
    ('You can have everything in life you want, if you will just '
     'help other people get what they want.'),
    'There is nothing like a challenge to bring out the best in man.',
    ('Optimism is the faith that leads to achievement. Nothing can '
     'be done without hope and confidence.')
]
AUTHORS = ['Zig Ziglar', 'Sean Connery', 'Helen Keller']


class QuoteTest(TestCase):

    def setUp(self):
        """Prep = add 3 quotes (source/cover = optional fields)"""
        for quote, author in zip(QUOTES, AUTHORS):
            Quote.objects.create(quote=quote, author=author)

    def test_count_objects_in_db(self):
        """Test if there are 3 objects in the temp DB table"""
        self.assertEqual(Quote.objects.count(), 3)

    def test_str_representation(self):
        """Check the output of the __str__ method"""
        quote = Quote.objects.get(author="Sean Connery")
        self.assertTrue(isinstance(quote, Quote))

        expected = ('There is nothing like a challenge to bring out '
                    'the best in man. - Sean Connery')
        self.assertEqual(str(quote), expected)

    def test_quotes_ordered_by_added_desc(self):
        """Check the working of the ordering as defined in the model's
           Meta class"""
        first = Quote.objects.first()
        last = Quote.objects.last()
        self.assertTrue(first.quote.startswith('Optimism'))
        self.assertEqual(last.author, 'Zig Ziglar')

    def test_quote_list_view(self):
        """Check if all quotes show up in the list view"""
        url = reverse("quotes:quote_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        content = resp.content.decode('utf-8')
        self.assertIn('<title>PyBites Quotes</title>', content)
        self.assertTrue(all(quote in content for quote in QUOTES))
        self.assertTrue(all(author in content for author in AUTHORS))

    def test_valid_form(self):
        """Test form with good and bad inputs"""
        # give optional fields = valid
        data = {'quote': 'Good Artists Copy; Great Artists Steal',
                'author': 'Pablo Picasso',
                'source': 'https://quoteinvestigator.com/2013/03/06/artists-steal/',  # noqa E501
                'cover': 'http://media.bsix12.com/2011/05/picasso-great-artists-steal.jpg'}  # noqa E501
        form = QuoteForm(data=data)
        self.assertTrue(form.is_valid())

        # go over author max len = invalid
        data = {'quote': 'Good Artists Copy; Great Artists Steal',
                'author': 'Pablo Picasso' * 10}
        form = QuoteForm(data=data)
        self.assertFalse(form.is_valid())
