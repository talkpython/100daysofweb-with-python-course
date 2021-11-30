import quart
from services import weather_service, sun_service, location_service

# Post video edit ****************************************
# Flask 2.0+ started raising an error on Blueprint(__name__, __name__)
# ValueError: 'name' may not contain a dot '.' character.
blueprint = quart.blueprints.Blueprint(__name__.replace('.', '_'), __name__)


@blueprint.route('/api/weather/<zip_code>/<country>', methods=['GET'])
async def weather(zip_code: str, country: str):
    if not weather_service.__api_key:
        return quart.jsonify({'status': 'disabled', 'reason': 'no API key'})

    weather_data = await weather_service.get_current(zip_code, country)
    if not weather_data:
        quart.abort(404)

    return quart.jsonify(weather_data)


@blueprint.route('/api/sun/<zip_code>/<country>', methods=['GET'])
async def sun(zip_code: str, country: str):
    lat, long = await location_service.get_lat_long(zip_code, country)
    sun_data = await sun_service.for_today(lat, long)
    if not sun_data:
        quart.abort(404)
    return quart.jsonify(sun_data)
