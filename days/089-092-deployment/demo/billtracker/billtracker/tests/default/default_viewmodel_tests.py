import unittest
import unittest.mock

from pyramid import testing
from pyramid.request import Request

from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.viewmodels.default.bill_details_viewmodel import BillDetailsViewModel
from billtracker.viewmodels.default.index_viewmodel import IndexViewModel


class ViewModelTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_index_viewmodel(self):
        # AAA's

        # Arrange
        request: Request = testing.DummyRequest()
        test_user = User()
        test_user.id = 1
        test_user.bills = [Bill(), Bill(), Bill()]

        # Act
        with unittest.mock.patch('billtracker.data.repository.get_user_by_id',
                                 return_value=test_user):
            vm = IndexViewModel(request, user_id=1)

        # Assert
        self.assertIsNone(vm.error)
        self.assertIsNotNone(vm.user)

    def test_details_vm_valid(self):
        request: Request = testing.DummyRequest()

        mock_user = User()
        mock_user.id = 74

        bill = Bill()
        bill.id = 700
        bill.user_id = mock_user.id
        request.matchdict['bill_id'] = bill.id

        mock_user.bills = [bill]

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id', return_value=mock_user)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id', return_value=bill)

        with p1, p2:
            vm = BillDetailsViewModel(request, mock_user.id)
            self.assertIsNone(vm.error)
            self.assertIsNotNone(vm.user)
            self.assertIsNotNone(vm.bill)
            self.assertEqual(vm.bill.id, bill.id)

    def test_details_vm_no_bill(self):
        request: Request = testing.DummyRequest()

        mock_user = User()
        mock_user.id = 74
        request.matchdict['bill_id'] = 200

        mock_user.bills = [Bill()]

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id', return_value=mock_user)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id', return_value=None)

        with p1, p2:
            vm = BillDetailsViewModel(request, mock_user.id)
            self.assertIsNotNone(vm.error)
            self.assertIn('The bill with ID {} was not found'.format(200), vm.error)

    def test_details_vm_no_user(self):
        request: Request = testing.DummyRequest()

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id', return_value=None)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id', return_value=None)

        with p1, p2:
            user_id = 10
            vm = BillDetailsViewModel(request, user_id)
            self.assertIsNotNone(vm.error)
            self.assertIn('No user with ID {}'.format(user_id), vm.error)

    def test_details_vm_bill_not_from_user(self):
        request: Request = testing.DummyRequest()

        mock_user = User()
        mock_user.id = 74

        bill = Bill()
        bill.id = 700
        bill.user_id = mock_user.id + 1
        request.matchdict['bill_id'] = bill.id

        mock_user.bills = [bill]

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id', return_value=mock_user)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id', return_value=bill)

        with p1, p2:
            vm = BillDetailsViewModel(request, mock_user.id)
            self.assertIsNotNone(vm.error)
            self.assertIsNone(vm.bill)
            self.assertIn('does not belong to user', vm.error)
