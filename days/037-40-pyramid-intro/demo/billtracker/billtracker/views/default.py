from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from billtracker.data import repository


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(_: Request):
    user_id = 1  # probably get from a cookie?

    user = repository.get_user_by_id(user_id)
    return {
        'user': user,
    }


@view_config(route_name='details',
             renderer='../templates/home/details.pt',
             request_method='GET')
def details_get(request: Request):
    bill_id = int(request.matchdict.get('bill_id'))
    bill = repository.get_bill_by_id(bill_id)
    if not bill:
        return Response(status=404)

    user_id = 1  # probably get from a cookie?
    user = repository.get_user_by_id(user_id)

    return {
        'user': user,
        'bill': bill,
        'error': None
    }


@view_config(route_name='details',
             renderer='../templates/home/details.pt',
             request_method='POST')
def details_post(request: Request):
    bill_id = int(request.matchdict.get('bill_id'))
    bill = repository.get_bill_by_id(bill_id)
    if not bill:
        return Response(status=404)

    user_id = 1  # probably get from a cookie?
    user = repository.get_user_by_id(user_id)

    amount = int(request.POST.get('amount', -1))
    if amount < 0 or amount > bill.total-bill.paid:
        error = 'Your amount must be more the zero and less than what you owe.'

        return {
            'user': user,
            'bill': bill,
            'error': error,
            'amount': amount
        }

    repository.add_payment(amount, bill_id)

    return HTTPFound(location='/bill/{}'.format(bill_id))
