# Star Wars Planet Browser

A flask app which retrieves and displays the Star Wars API (SWAPI) planet data.
I made this app to learn how to use APIs and pytest. This is also the first app I've deployed to Heroku.

(View App)[https://secure-ocean-16983.herokuapp.com/]

### API
BasicApi class: retrieves the data from SWAPI and caches it. 
I've tried to make this as reusable as possible for other APIs. I added caching as the requests were taking a few seconds to return data.

Planet class: takes the dictionary returned by the BasicApi class and uses the data to create a Planet object.

### App
The app only has one route at the moment which is for the index page to display all the planet cards.


What I learned:
* Setting up linting in VSCode with Flake8 and changing settings
* Using requests to get data from an API
* Caching the response
* Creating tests and fixtures with pytest
* Deploying to Heroku

Resources:
(SWAPI Planets Documentation)[https://swapi.dev/documentation#planets]
(How to use APIs)[https://realpython.com/api-integration-in-python/]
(Caching)[https://realpython.com/caching-external-api-requests/]
(Deploying a Flask app to Heroku)[https://realpython.com/flask-by-example-part-1-project-setup/]