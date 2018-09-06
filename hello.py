from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(2+3)
    return '<h1>Hello, my very best friend!!!!!!!</h1>'
