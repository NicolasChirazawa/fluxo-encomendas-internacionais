from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 

from infra.object_value.date_object import DateObjectBuild
from infra.enum.country_currency import Currency
from infra.exchange_rate.exchange_rate_factory import ExchangeRateDataFactory

import json
from urllib.request import urlopen, Request

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRate:
    def __init__(self):
        self.date = ""
        self.originCurrency = ""
        self.shippingCurrency = ""
        self.exchangeRate = ""

class ExchangeRateBuild:
    def __init__(self):
        self._exchangeRateData = ExchangeRate()

    def setDate(self, date):
        self._exchangeRateData.date = (
            DateObjectBuild()
            .setDate(date)
            .setElementsDate()
            .build()
        )

        return self

    def setOriginCurrency(self):
        country  = CONFIGURATION_JSON["LOCALE"]["COUNTRY"]
        country = country.upper()
        self._exchangeRateData.originCurrency = Currency[country].value

        return self

    def setShippingCurrency(self, country):
        country = country.upper()
        self._exchangeRateData.shippingCurrency = Currency[country].value

        return self

    def setExchangeRate(self):
        origen_currency   = self._exchangeRateData.originCurrency
        shipping_currency = self._exchangeRateData.shippingCurrency

        date_format_exchange_rate = (
            self._exchangeRateData.date.year + 
            "-" + 
            self._exchangeRateData.date.month + 
            "-" + 
            self._exchangeRateData.date.day
        )

        exchange_rate_value = ExchangeRateDataFactory.get(origen_currency, shipping_currency, date_format_exchange_rate)

        if exchange_rate_value == None:
            exchange_rate_value = self.searchFrankFurterAPI(origen_currency, shipping_currency, date_format_exchange_rate)
            ExchangeRateDataFactory.set(origen_currency, shipping_currency, date_format_exchange_rate, exchange_rate_value)

        self._exchangeRateData.exchangeRate = exchange_rate_value
        return self

    def searchFrankFurterAPI(self, origen_currency, shipping_currency, date_format_exchange_rate):
        exchangeRateURL = f"https://api.frankfurter.dev/v2/rates?base={shipping_currency}&quotes={origen_currency}&date={date_format_exchange_rate}"
        
        request = Request(
            exchangeRateURL,
            headers={
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urlopen(request) as response:
            raw_data = response.read().decode("utf-8")
            
            data = json.loads(raw_data)

        return data[0]["rate"]

    def build(self):
        return self._exchangeRateData
