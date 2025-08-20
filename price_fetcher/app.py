from flask import Flask, jsonify
import requests

app = Flask(__name__)

COINS = ['bitcoin', 'ethereum', 'dogecoin']

@app.route('/prices')
def get_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': ','.join(COINS), 'vs_currencies': 'usd'}
    response = requests.get(url, params=params)
    prices = response.json()
    return jsonify(prices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
