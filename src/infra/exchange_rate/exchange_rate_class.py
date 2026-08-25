from src.infra.object_value.date_object import DateObjectBuild
from infra.object_value.country_currency import Currency

import json
from urllib.request import urlopen, Request

class ExchangeRateData:
    def __init__(self):
        self.date = ""
        self.currency = ""
        self.exchangeRate = ""

class ExchangeRateDataBuild:
    def __init__(self):
        self._exchangeRateData = ExchangeRateData()

    def setDate(self, date):
        self._exchangeRateData.date = (DateObjectBuild()
            .setDate(date)
            .setElementsDate()
            .build()
            )

        return self

    def setCurrency(self, country):
        country = country.upper()
        self._exchangeRateData.currency = Currency[country].value

        return self

    def setExchangeRate(self):
        dateFormatExchangeRate = f"{self._exchangeRateData.date.year}-{self._exchangeRateData.date.month}-{self._exchangeRateData.date.day}"
        currency = self._exchangeRateData.currency

        exchangeRateURL = f"https://api.frankfurter.dev/v2/rates?base={currency}&quotes=BRL&date={dateFormatExchangeRate}"

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

        self._exchangeRateData.exchangeRate = data[0]["rate"]
        return self

    def build(self):
        return self._exchangeRateData
