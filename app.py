import click
from flask import Flask
import click
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    with open('environment.txt') as f:
        data = f.readline()
    return f'Привет!\n{data}'


@app.cli.command("chtext")
@click.argument("text", nargs=-1)
def chtext(text):
    message = ' '.join(list(text))
    with open('environment.txt', 'w') as f:
        f.write(message)


if __name__ == '__main__':
    app.run()
