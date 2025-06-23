from flask import Flask, jsonify, request
from .database import db_session, init_db
from .models import User, Item, PriceHistory
import os
import requests

app = Flask(__name__)

STEAM_API_KEY = os.environ.get('STEAM_API_KEY')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/inventory')
def get_inventory():
    steamid = request.args.get('steamid')
    if not steamid:
        return jsonify({'error': 'steamid required'}), 400
    # Example call to Steam Web API
    if not STEAM_API_KEY:
        return jsonify({'error': 'STEAM_API_KEY not configured'}), 500
    url = (
        f"https://api.steampowered.com/IPlayerService/"
        f"GetOwnedGames/v1/?key={STEAM_API_KEY}&steamid={steamid}"
    )
    try:
        resp = requests.get(url)
        data = resp.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify(data)

@app.route('/prices')
def get_prices():
    item_name = request.args.get('item')
    if not item_name:
        return jsonify({'error': 'item required'}), 400
    # Query database for price history
    history = PriceHistory.query.filter_by(item_name=item_name).all()
    return jsonify([h.as_dict() for h in history])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
