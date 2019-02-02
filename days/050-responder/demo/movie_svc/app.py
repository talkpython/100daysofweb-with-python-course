# noinspection PyUnresolvedReferences
from data import db
# noinspection PyUnresolvedReferences
from api_instance import api
# noinspection PyUnresolvedReferences
from views.home import *
from views.api_views import *


def main():
    db.global_init()

    api.run()


if __name__ == '__main__':
    main()
