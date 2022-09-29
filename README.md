# Star Wars Planet Browser

A flask app which retrieves and displays the Star Wars API (SWAPI) planet data.
I made this app to learn how to use APIs and pytest. This is also the first app I've deployed to Heroku.

[View App](https://secure-ocean-16983.herokuapp.com/)

### Run locally

1. Clone the repository
2. Run setup.sh (command: bash setup.sh). This will create the virtual environment and install requirments.
3. Activate the virtual environment (command: source venv/bin/activate)
4. Run the app (command: flask run)
5. Open a browser and go to http://localhost:5000/

### API

BasicApi class: retrieves the data from SWAPI and caches it.
I've tried to make this as reusable as possible for other APIs. I added caching as the requests were taking a few seconds to return data.

Planet class: takes the dictionary returned by the BasicApi class and uses the data to create a Planet object.

### App

The main page displays all planets. These can be filtered by climate or terrain by clicking on the links in these fields.

What I learned:

- Setting up linting in VSCode with Flake8 and changing settings
- Using requests to get data from an API
- Caching the response
- Creating routes for variable URLs
- Creating tests and fixtures with pytest
- Improved CSS layout skills
- Deploying to Heroku

Resources:

- [SWAPI Planets Documentation](https://swapi.dev/documentation#planets)
- [How to use APIs](https://realpython.com/api-integration-in-python/)
- [Caching](https://realpython.com/caching-external-api-requests/)
- [Deploying a Flask app to Heroku](https://realpython.com/flask-by-example-part-1-project-setup/)
