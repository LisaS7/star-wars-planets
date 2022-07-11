import requests
import requests_cache
import configparser
from datetime import timedelta


# __________CONFIG__________
config = configparser.ConfigParser()
config.read('config.ini')


# __________FUNCTIONS__________
def get_page_json(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None


def get_int_from_dict(dict, key):
    try:
        number = int(dict[key])
    except ValueError:
        print(f'Data type of {dict[key]} is not a number')
    return number


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
                content_list.append(response[self.content])
        else:
            print('No next page URL found.')

        return content_list


class Planet:
    def __init__(self, dict):
        self.name = dict['name']
        self.day_length = timedelta(hours=get_int_from_dict(dict, 'rotation_period'))
        self.year_length = timedelta(days=get_int_from_dict(dict, 'orbital_period'))

    def __repr__(self):
        return f'{self.name}, {self.day_length}'


if __name__ == '__main__':
    SWAPI = BasicApi('SWAPI')

    planet_data = SWAPI.get_all_pages()
    planets = []

    for planet in planet_data[0:5]:
        print(planet)
        planets.append(Planet(planet))

    print(planets)
