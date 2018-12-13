import unittest


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
        urls = [
            '/',
            '/bill/386',
            '/bill/351',
        ]

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
