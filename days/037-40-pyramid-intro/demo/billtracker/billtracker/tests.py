import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views.default import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info['project'], 'Bill Tracker Pro')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from billtracker import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
