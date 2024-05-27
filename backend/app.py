from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def home():
    theme = request.cookies.get("theme")
    print(theme)
    return f"<h1>Hello World</h1> <h2>{theme if theme=='dark' else ''}</h2>"


@app.route('/cookie')
def cookie():
    res = make_response("<h1>Cookie is set</h1>")
    res.set_cookie("theme", "dark")
    return res
