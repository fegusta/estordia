#!/usr/bin/env python3
"""Periodic data updater."""

from backend.database import db_session, init_db
from backend.models import Item, PriceHistory
import requests
import os
import time

STEAM_API_KEY = os.environ.get('STEAM_API_KEY')


def fetch_prices(item_name):
    # Placeholder: implement actual fetch from Steam and external sources
    return {
        'steam': 0.0,
        'external': 0.0,
    }


def main():
    init_db()
    items = db_session.query(Item).all()
    for item in items:
        prices = fetch_prices(item.name)
        for source, price in prices.items():
            history = PriceHistory(item_name=item.name, source=source, price=price)
            db_session.add(history)
    db_session.commit()

if __name__ == '__main__':
    main()
