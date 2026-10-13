from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 
from infra.object_value.date_object import DateObjectBuild
from infra.enum.country_currency import Currency

import json
from urllib.request import urlopen, Request

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRateData:
    def __init__(self):
        self.date = ""
        self.originCurrency = ""
        self.shippingCurrency = ""
        self.exchangeRate = ""

class ExchangeRateDataBuild:
    def __init__(self):
        self._exchangeRateData = ExchangeRateData()

    def setDate(self, date):
        self._exchangeRateData.date = (
            DateObjectBuild()
            .setDate(date)
            .setElementsDate()
            .build()
        )

        return self

    def setOriginCurrency(self):
        country = CONFIGURATION_JSON["ORIGIN_COUNTRY"]
        country = country.upper()
        self._exchangeRateData.originCurrency = Currency[country].value

        return self

    def setShippingCurrency(self, country):
        country = country.upper()
        self._exchangeRateData.shippingCurrency = Currency[country].value

        return self

    def setExchangeRate(self):
        origenCurrency   = self._exchangeRateData.originCurrency
        shippingCurrency = self._exchangeRateData.shippingCurrency

        dateFormatExchangeRate = (
            self._exchangeRateData.date.year + 
            "-" + 
            self._exchangeRateData.date.month + 
            "-" + 
            self._exchangeRateData.date.day
        )

        if 

        exchangeRate = self.searchFrankFurterAPI(origenCurrency, shippingCurrency, dateFormatExchangeRate)

        self._exchangeRateData.exchangeRate = exchangeRate
        return self

    def searchFrankFurterAPI(self, shippingCurrency, origenCurrency, dateFormatExchangeRate):
        exchangeRateURL = f"https://api.frankfurter.dev/v2/rates?base={shippingCurrency}&quotes={origenCurrency}&date={dateFormatExchangeRate}"
        
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
