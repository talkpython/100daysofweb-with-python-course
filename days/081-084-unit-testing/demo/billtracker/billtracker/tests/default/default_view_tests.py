import unittest
import unittest.mock

from pyramid import testing
from pyramid.request import Request

from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_index(self):
        # AAA's

        # Arrange
        from billtracker.views.default import home
        request: Request = testing.DummyRequest()
        test_user = User()
        test_user.id = 1
        test_user.bills = [Bill(), Bill(), Bill()]

        # Act
        with unittest.mock.patch('billtracker.data.repository.get_user_by_id',
                                 return_value=test_user):
            info = home(request)

        # Assert
        self.assertIsNotNone(info['user'])

    def test_details_get(self):
        from billtracker.views.default import details_get

        request: Request = testing.DummyRequest()
        user_id = 72
        request.matchdict['bill_id'] = 700

        mock_user = User()
        mock_user.id = user_id
        mock_user.bills = [Bill(), Bill(), Bill()]
        for b in mock_user.bills:
            b.user_id = user_id

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id',
                                 return_value=mock_user)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id',
                                 return_value=mock_user.bills[0])

        with p1, p2:
            info = details_get(request)

        self.assertIsNotNone(info['user'])
        self.assertGreater(len(info['user'].bills), 0)
