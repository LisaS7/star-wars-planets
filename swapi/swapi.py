from pathlib import Path
import requests
import requests_cache
from datetime import timedelta


# __________CONFIG__________
URL = 'https://swapi.dev/api/planets/'
CACHE_NAME = 'planet_cache'
CACHE_EXPIRY_DAYS = 30
CONTENT_LABEL = 'results'
NEXT_URL_LABEL = 'next'


# __________FUNCTIONS__________
def get_page_json(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None


def set_timedelta(number, units):
    if isinstance(number, str):
        raise TypeError(f'Convert string {number} to number before setting timedelta.')
    if number is None:
        return None
    elif units == 'hours':
        return timedelta(hours=number)
    elif units == 'days':
        return timedelta(days=number)


def create_planets(data):
    return [Planet(planet) for planet in data]


# __________CLASSES__________
class BasicApi:
    def __init__(self, API):
        self.api = API
        self.url = URL
        self.content = CONTENT_LABEL
        self.next_url = NEXT_URL_LABEL
        self.create_cache()

    def create_cache(self):
        cache_expiry_days = CACHE_EXPIRY_DAYS

        requests_cache.install_cache(
            cache_name=CACHE_NAME,
            backend='sqlite',
            expire_after=timedelta(days=cache_expiry_days)
        )

    def get_all_pages(self):
        response = get_page_json(self.url)
        content_list = response[self.content]

        if response[self.next_url]:
            while response[self.next_url]:
                response = get_page_json(response[self.next_url])
                content_list.extend(response[self.content])
        else:
            print('No next page URL found.')

        return content_list


class Planet:
    def __init__(self, data_dict):
        self.data = data_dict
        self.name = data_dict['name']
        self.day_length = set_timedelta(self.int_from_key('rotation_period'), 'hours')
        self.year_length = set_timedelta(self.int_from_key('orbital_period'), 'days')
        self.climate = self.list_from_string('climate')
        self.terrain = self.list_from_string('terrain')
        self.surface_water = self.int_from_key('surface_water')
        self.population = self.int_from_key('population')
        self.gravity = data_dict['gravity']

    def __repr__(self):
        return f'{self.name}'

    def int_from_key(self, key):
        try:
            number = int(self.data[key])
            return number
        except ValueError:
            return None

    def list_from_string(self, key):
        return [item.strip() for item in self.data[key].split(',')]
