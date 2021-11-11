# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="localhost",port=5000)