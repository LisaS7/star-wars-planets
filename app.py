from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=TRUE)