import requests
import requests_cache
from datetime import timedelta

API_URL = 'https://swapi.dev/api/planets/'
CACHE_EXPIRE_AFTER = timedelta(days=30)

requests_cache.install_cache(cache_name='planet_cache', backend='sqlite', expire_after=CACHE_EXPIRE_AFTER)


response = requests.get(API_URL).json()
# print(response.json())

planet_list = response['results']

print(planet_list)

while response['next']:
    response = requests.get(response['next']).json()
    planet_list.append(response['results'])

for planet in planet_list[0:3]:
    print(planet)