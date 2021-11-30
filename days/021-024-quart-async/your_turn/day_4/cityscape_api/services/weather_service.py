import requests

# TODO: Set your api.openweathermap.org API key here:
__api_key = ''


def global_init(api_key: str):
    global __api_key
    __api_key = api_key

    if not api_key:
        print("Warning: No weather API key.")
        print("If you want the weather part of the API to work, please get your own API key (free).")
        print("It's available at https://api.openweathermap.org -- just sign up.")
        print()


def get_current(zip_code: str, country_code: str) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={__api_key}'
    resp = requests.get(url)
    resp.raise_for_status()

    return resp.json()
