import responder

api = responder.API()


# api.static_route('/static', static=True)

@api.route('/')
def index(req, resp):
    resp.content = api.template('home/index.html')


@api.route('/api/search/{keyword}')
def search_by_keyword(req, resp: responder.Response, keyword: str):
    resp.media = {'searching': keyword}


@api.route('/api/director/{director_name}')
def search_by_director(req, resp: responder.Response, director_name: str):
    resp.media = {'searching': director_name}


@api.route('/api/movie/{imdb_number}')
def movie_by_imdb(req, resp: responder.Response, imdb_number: str):
    resp.media = {'searching': imdb_number}


api.run()
