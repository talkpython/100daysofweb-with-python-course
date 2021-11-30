import flask
from views import city_api
from views import home
from config import settings
import services.weather_service
import services.sun_service
import services.location_service

app = flask.Flask(__name__)
is_debug = False

app.register_blueprint(home.blueprint)
app.register_blueprint(city_api.blueprint)


def configure_app():
    mode = 'dev' if is_debug else 'prod'
    data = settings.load(mode)

    services.weather_service.global_init(data.get('weather_key', ''))
    services.sun_service.use_cached_data = data.get('use_cached_data', False)

    # Sadly, datasciencetoolkit.org seems to have gone out of existence.
    services.location_service.use_cached_data = True

    print("Using cached data? {}".format(data.get('use_cached_data', False)))


def run_web_app():
    app.run(debug=is_debug, port=5001)


configure_app()

if __name__ == '__main__':
    run_web_app()
