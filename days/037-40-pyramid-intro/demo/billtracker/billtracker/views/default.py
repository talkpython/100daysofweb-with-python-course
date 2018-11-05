from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(request):
    # access the db or web services
    return {
        'project': 'Bill Tracker Pro Demo',
        'items': [
            'item1', 'item2', 'item3', 'item4'
        ]

    }
