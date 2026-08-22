from src.infra.object_value.date_object import DateObjectBuild

import json
from urllib.request import urlopen, Request

class ExchangeRateData:
    def __init__(self):
        self.date = ''
        self.exchangeRate = ''

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

    def setExchangeRate(self):
        dateFormatExchangeRate = self._exchangeRateData.date.year + '-' + self._exchangeRateData.date.month + '-' + self._exchangeRateData.date.day

        exchangeRateURL = "https://api.frankfurter.dev/v2/rates?base=JPY&quotes=BRL&date=" + dateFormatExchangeRate

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

        self._exchangeRateData.exchangeRate = data[0]['rate']
        return self

    def build(self):
        return self._exchangeRateData
