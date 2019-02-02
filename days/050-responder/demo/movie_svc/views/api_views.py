import responder

from api_instance import api
from data import db

response_count_max = 10


@api.route('/api/search/{keyword}')
def search_by_keyword(_, resp: responder.Response, keyword: str):
    movies = db.search_keyword(keyword)
    print("Searching for movie by keyword: {}".format(keyword))

    limited = len(movies) > response_count_max
    if limited:
        movies = movies[:10]

    movie_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {'keyword': keyword, 'hits': movie_dicts, 'truncated_results': limited}


@api.route('/api/director/{director_name}')
def search_by_director(_, resp: responder.Response, director_name: str):
    movies = db.search_director(director_name)
    print("Searching for movie by director: {}".format(director_name))

    limited = len(movies) > response_count_max
    if limited:
        movies = movies[:10]

    movie_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {'keyword': director_name, 'hits': movie_dicts, 'truncated_results': limited}


@api.route('/api/movie/{imdb_number}')
def movie_by_imdb(_, resp: responder.Response, imdb_number: str):
    movie = db.find_by_imdb(imdb_number)
    resp.media = db.movie_to_dict(movie)
