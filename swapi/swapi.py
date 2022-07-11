from pathlib import Path
import requests
import requests_cache
import configparser
from datetime import timedelta


# __________CONFIG__________
config = configparser.ConfigParser()
config.read(Path.cwd().parent / 'config.ini')


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
        self.url = None
        self.content = None
        self.next_url = None
        self.config()
        self.create_cache()

    def config(self):
        try:
            self.url = config.get(self.api, 'URL')
            self.content = config.get(self.api, 'CONTENT_LABEL')
            self.next_url = config.get(self.api, 'NEXT_URL_LABEL')
        except configparser.NoSectionError:
            print('API not defined in config.ini')
        except Exception as e:
            print(e)

    def create_cache(self):
        cache_expiry_days = int(config.get(self.api, 'CACHE_EXPIRY_DAYS'))

        requests_cache.install_cache(
            cache_name=config.get(self.api, 'CACHE_NAME'),
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


# __________RUN__________
if __name__ == '__main__':

    SWAPI = BasicApi('SWAPI')

    planet_data = SWAPI.get_all_pages()
    planets = create_planets(planet_data)

    print(planets)
