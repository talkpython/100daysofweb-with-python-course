from api_instance import api


# api.static_route('/static', static=True)

@api.route('/')
def index(_, resp):
    resp.content = api.template('home/index.html')
