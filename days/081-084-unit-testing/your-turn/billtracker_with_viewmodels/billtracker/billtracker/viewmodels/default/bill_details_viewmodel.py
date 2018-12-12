from pyramid.request import Request

from billtracker.viewmodels.viewmodelbase import ViewModelBase
from billtracker.data import repository


class BillDetailsViewModel(ViewModelBase):

    def __init__(self, request: Request, user_id: int):
        super().__init__(request)

        self.bill_id = int(request.matchdict.get('bill_id'))
        self.bill = repository.get_bill_by_id(self.bill_id)

        self.user_id = user_id
        self.user = repository.get_user_by_id(user_id)
        self.amount = None

    def from_form(self):
        try:
            self.amount = int(self.request.POST.get('amount', -1))
            if self.amount < 0 or self.amount > self.bill.total - self.bill.paid:
                self.error = 'Your amount must be more the zero and less than what you owe.'
        except:
            self.error = "Amount must be an integer."
