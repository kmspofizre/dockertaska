import click
from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return f'Привет!'


if __name__ == '__main__':
    app.run()
