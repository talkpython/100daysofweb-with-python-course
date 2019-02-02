import responder

api = responder.API()


# api.static_route('/static', static=True)

@api.route('/')
def index(req, resp):
    resp.content = api.template('home/index.html')


api.run()
