from pyramid.request import Request
from pyramid.view import view_config

from billtracker.data import repository


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(_: Request):
    user_id = 1  # probably get from a cookie?

    user = repository.get_user_by_id(user_id)
    return {
        'user': user,
    }
