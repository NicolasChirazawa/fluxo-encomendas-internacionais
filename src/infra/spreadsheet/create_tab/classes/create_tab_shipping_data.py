from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['language'])

class TabShippingData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName",
            "shippingDateLimit", 
            "shippingCountry", 
            "shippingDate", 
            "shippingCurrencyPrice", 
            "shippingCurrencyServiceTax", 
            "shippingPaymentMethod", 
            "shippingQuote", 
            "shippingPrice", 
            "shippingStatus"
        ]
        self.dataframe = ""

class TabShippingDataBuilder:
    def __init__(self):
        self._tabShippingData = TabShippingData()

    def setType (self, type):
        self._tabShippingData.type = type
        return self

    def setTabName (self, tabName):
        self._tabShippingData.tabName = tabName
        return self

    def setDataframe (self, data):
        self._tabShippingData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabShippingData.newOrderColumns)
            .rename(LANGUAGE_JSON['SPREADSHEET'][self._tabShippingData.type]["COLUMNS"])
            .build()
        )
        return self

    def build(self):
        return self._tabShippingData
