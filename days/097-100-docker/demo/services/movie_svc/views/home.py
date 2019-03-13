from app_instance import api


@api.route("/")
def index(req, resp):
    resp.content = api.template('home/index.html')
