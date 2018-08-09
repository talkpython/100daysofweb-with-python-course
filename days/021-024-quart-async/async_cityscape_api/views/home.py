import quart

blueprint = quart.blueprints.Blueprint(__name__, __name__)


@blueprint.route('/')
def index():
    return "Welcome to the city_scape API. Use /api/city/* for API calls."


@blueprint.errorhandler(404)
def not_found(_):
    return quart.Response("The page was not found.", status=404)
