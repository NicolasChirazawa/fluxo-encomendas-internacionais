import os
import json
from infra.json.read_json import readJSON

ARCHIVE_FILE = os.path.join(os.path.abspath(""), "infra", "exchange_rate", "local", "exchange_rate_cache.json")

def get (origen_currency, shipping_currency, date_format_exchange_rate):
    JSON_data = readJSON(ARCHIVE_FILE)

    currency_key = origen_currency + "_" + shipping_currency
    exchange_rate_cache = JSON_data.get(currency_key, {}).get(date_format_exchange_rate)

    return exchange_rate_cache

def set (origen_currency, shipping_currency, date_format_exchange_rate, exchange_rate_value):
    JSON_data = readJSON(ARCHIVE_FILE)

    currency_key = origen_currency + "_" + shipping_currency

    if currency_key not in JSON_data:
        JSON_data[currency_key] = {}

    # Change dict in runtime
    JSON_data[currency_key][date_format_exchange_rate] = exchange_rate_value

    # Change file with new values
    JSON_data_new = json.dumps(JSON_data)
    with open(ARCHIVE_FILE, "w") as f:
        f.write(JSON_data_new)

    return None
    