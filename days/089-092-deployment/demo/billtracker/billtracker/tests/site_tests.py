import unittest
from typing import List

from billtracker.data import repository
from billtracker.data.models.bill import Bill


class SiteTests(unittest.TestCase):
    def setUp(self):
        from billtracker import main
        app = main({})
        from webtest import TestApp
        self.app = TestApp(app)

    def test_root(self):
        res = self.app.get('/', status=200)
        self.assertTrue(b'Dannie Easom' in res.body)
        self.assertTrue(b'Unpaid bills' in res.body)

    def test_sitemap(self):
        # Update the way we find the bills for this user.
        # Turns out the ID varies depending on how you populate
        # the DB.
        urls = [
            '/'
        ]
        user = repository.get_user_by_id(1)
        bills: List[Bill] = user.bills
        for b in bills:
            urls.append('/bill/{}'.format(b.id))

        for url in urls:
            self.app.get(url, status=200)

    def test_sitemap_other(self):
        # We don't really have a sitemap, but often sites do. You can simply
        # request every page in your sitemap as a way to verify it's generally
        # hanging together.
        #
        # Here is some example code from another course:
        #
        #   https://github.com/talkpython/data-driven-web-apps-with-pyramid-and-sqlalchemy/blob/master/src/ch14-testing/final/pypi_testing/pypi/tests/sitemap_tests.py
        #
        pass
