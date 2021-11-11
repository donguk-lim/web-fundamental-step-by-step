# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def throw():
    return render_template("throw.html")

@app.route("/catch/", methods=["POST"])
def catch():
    name = request.values.get("name")
    hobby = request.values.get("hobby")
    context = {}
    context["name"] = name
    context["hobby"] = hobby
    return render_template("catch.html", **context)

if __name__ == "__main__":
    app.run(host="localhost",port=5000)