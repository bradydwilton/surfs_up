from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


test = Flask(__name__)


@app.route('/test')
def testing():
    return 'this shit is testing'


@app.route('/btc')
def btc():
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')

    btc = int(response.json()['bitcoin']['usd'])

    return f'{btc}'
