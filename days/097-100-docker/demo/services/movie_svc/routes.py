# noinspection PyUnresolvedReferences
from app_instance import api
# noinspection PyUnresolvedReferences
from views.api_views import *
# noinspection PyUnresolvedReferences
from views.home import *

api.add_route("/static", static=True)
