from flask import Flask, render_template
from swapi.swapi import BasicApi, create_planets

app = Flask(__name__)


SWAPI = BasicApi('SWAPI')

planet_data = SWAPI.get_all_pages()
planets = create_planets(planet_data)


@app.route("/")
def hello_world():
    print(planets)
    return render_template('index.html', planets=planets)


if __name__ == '__main__':

    app.run()
