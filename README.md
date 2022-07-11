# Star Wars Planet Browser

A flask app to practise using REST APIs with the Star Wars API (SWAPI) planet data.

### swapi.py 
BasicApi class: retrieves the data from SWAPI and caches it. 
I've tried to make this as reusable as possible for other APIs. I added caching and a separate config.ini file (probably overkill but I wanted to learn how to use configparser).

Planet class: takes the dictionary returned by the BasicApi class and uses the data to create a Planet object.


What I learned:
* Setting up linting in VSCode with Flake8 and changing settings
* Using requests to get data from an API
* Caching the response
* Using a config.ini file with configparser
* Creating tests and fixtures with pytest

Resources:
(SWAPI Planets Documentation)[https://swapi.dev/documentation#planets]
(How to use APIs)[https://realpython.com/api-integration-in-python/]
(Caching)[https://realpython.com/caching-external-api-requests/]