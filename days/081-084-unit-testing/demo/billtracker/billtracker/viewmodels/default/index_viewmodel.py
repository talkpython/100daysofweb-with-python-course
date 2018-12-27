from pyramid.request import Request

from billtracker.data import repository
from billtracker.viewmodels.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):

    def __init__(self, request: Request, user_id: int):
        super().__init__(request)

        self.user_id = user_id
        self.user = repository.get_user_by_id(user_id)

        if not self.user:
            self.error = "No user with ID {}.".format(user_id)
