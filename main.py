import click
from flask import Flask
import docker
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = docker.from_env()
url = str(os.getenv('URL'))
port = str(os.getenv('PORT'))


@app.route('/')
@app.route('/index')
def home():
    return f'''<!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                        <title>Привет</title>
                                      </head>
                                      <body>
                                        <h1 style="margin-top: 5px;">Привет</h1>
                                      </body>
                                    </html>'''


@app.cli.command("create")
@click.argument("name")
@click.argument("port")
def create(name, port):
    with open('environment.txt', 'w') as f:
        f.write(f'123\n123\n{name}')
    cont = client.containers.run('flask', None, name=name,
                                    ports={f'{5000}/tcp': ('127.0.0.1', port)}, detach=True,
                                    )
    cont.exec_run(f'flask chtext Меня зовут - {name}')
    cont.stop()


# cont1 = client.containers.run('alpine', 'sleep infinity',
#                              ports={'80/tcp': ('127.0.0.1', 1111)}, detach=True,
#                              )
# cont1.stop()
@app.cli.command("start")
@click.argument("name")
def start(name):
    cont = client.containers.get(name)
    cont.start()


@app.cli.command("stop")
@click.argument("name")
def stop(name):
    cont = client.containers.get(name)
    cont.stop()


@app.cli.command("log")
@click.argument("name")
def log(name):
    cont = client.containers.get(name)
    cont_logs = cont.logs()
    print(cont_logs)


@app.cli.command("send")
@click.argument("name")
@click.argument("message", nargs=-1)
def send(name, message):
    message = ' '.join(list(message))
    cont = client.containers.get(name)
    cont.exec_run(f'flask chtext {message}')


if __name__ == '__main__':
    app.run(port=port, host=url)
