import datetime
import random
import time

import requests

measured_latency_in_sec = [0.399203, 0.7046, 0.422959, 0.741911, 0.404674]
use_cached_data = False


def for_today(latitude: float, longitude: float) -> dict:
    url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}'

    if use_cached_data:  # Set in config/dev.json or config/prod.json
        # TODO: Convert this to await asyncio.sleep()

        time.sleep(random.choice(measured_latency_in_sec))
        return {'sunrise': '06:04:09 AM', 'sunset': '08:28:48 PM', 'solar_noon': '01:16:28 PM',
                'day_length': '14:24:39', 'civil_twilight_begin': '05:31:10 AM', 'civil_twilight_end': '09:01:47 PM',
                'nautical_twilight_begin': '04:49:54 AM', 'nautical_twilight_end': '09:43:03 PM',
                'astronomical_twilight_begin': '04:03:13 AM', 'astronomical_twilight_end': '10:29:44 PM'}
    else:
        resp = requests.get(url)
        resp.raise_for_status()

        sun_data = resp.json().get('results', {})
        for k, v in list(sun_data.items()):
            if 'AM' not in v and 'PM' not in v:
                continue

            sun_data[k] = datetime.datetime.strftime(__utc_to_local(v), '%I:%M:%S %p')

        return sun_data


def __utc_to_local(date_text: str) -> datetime.datetime:
    # Not perfect, but works most of the time.
    utc = datetime.datetime.strptime(date_text, '%I:%M:%S %p')
    now_timestamp = time.time()
    offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    return utc + offset
