from flask import Flask, jsonify
from random import uniform

app = Flask(__name__)

@app.route('/liquidity')
def simulate_liquidity():
    # Return simulated liquidity info with some random growth
    liquidity = {
        'total_liquidity_usd': round(1000000 * uniform(1.0, 1.05), 2),
        'growth_percent': round(uniform(0.1, 2.0), 2)
    }
    return jsonify(liquidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
