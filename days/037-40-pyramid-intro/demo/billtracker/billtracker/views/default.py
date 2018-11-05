from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(request):
    return {'project': 'Bill Tracker Pro'}
