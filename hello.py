from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("VISITED HOME PAGE")
    return "Hello, world"

@app.route("/about")
def about():
    print("VISITED ABOUT PAGE")
    return "About me:"

