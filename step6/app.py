# flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask, render_template, request

jinja_options = Flask.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>',
))

Flask.jinja_options = jinja_options


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
    app.run(host="localhost",port=5000, debug=True)