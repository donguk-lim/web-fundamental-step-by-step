# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost",port=5000)