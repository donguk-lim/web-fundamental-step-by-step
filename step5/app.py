# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def throw():
    return render_template("index.html")

@app.route("/catch/", methods=["POST"])
def catch():
    name = request.get_json().get("name")
    hobby = request.get_json().get("hobby")
    result = f"{name}은 {hobby}를 좋아합니다!!"
    return {"name": name, "hobby": hobby, "result":result}

if __name__ == "__main__":
    app.run(host="localhost",port=5000)