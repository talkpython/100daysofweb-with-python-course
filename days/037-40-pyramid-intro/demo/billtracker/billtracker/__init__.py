import os

from pyramid.config import Configurator

from billtracker.bin import load_base_data
from billtracker.data.db_session import DbSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()

    init_db()

    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'bill_tracker.sqlite'
    )
    DbSession.global_init(db_file)
    load_base_data.load_starter_data()
