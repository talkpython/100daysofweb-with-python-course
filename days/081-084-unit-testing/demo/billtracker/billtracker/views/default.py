from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from billtracker.data import repository
from billtracker.viewmodels.default.index_viewmodel import IndexViewModel
from billtracker.viewmodels.default.bill_details_viewmodel import BillDetailsViewModel


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(request: Request):
    vm = IndexViewModel(request, user_id=1)
    return vm.to_dict()


@view_config(route_name='details',
             renderer='../templates/home/details.pt',
             request_method='GET')
def details_get(request: Request):
    vm = BillDetailsViewModel(request, user_id=1)

    if not vm.bill:
        return Response(status=404)

    return vm.to_dict()


@view_config(route_name='details',
             renderer='../templates/home/details.pt',
             request_method='POST')
def details_post(request: Request):
    vm = BillDetailsViewModel(request, user_id=1)

    if not vm.bill:
        return Response(status=404)

    vm.from_form()

    if vm.error:
        return vm.to_dict()

    repository.add_payment(vm.amount, vm.bill_id)

    return HTTPFound(location='/bill/{}'.format(vm.bill_id))
