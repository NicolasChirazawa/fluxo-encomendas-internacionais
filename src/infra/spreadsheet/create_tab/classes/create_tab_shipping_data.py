from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from infra.spreadsheet.spreadsheet_template import SpreadsheetTemplateBuild

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON["LOCALE"]["LANGUAGE"])

class TabShipData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName",
            "shipDateLimit", 
            "shipCountry", 
            "shipDate", 
            "shipCurrencyPrice", 
            "shipCurrencyServiceTax", 
            "shipPaymentMethod", 
            "shipQuote", 
            "shipPrice", 
            "shipStatus"
        ]
        self.dataframe = ""

class TabShipDataBuilder:
    def __init__(self):
        self._tabShipData = TabShipData()

    def setType (self, type):
        self._tabShipData.type = type
        return self

    def setTabName (self, tabName):
        self._tabShipData.tabName = tabName
        return self

    def setDataframe (self, data):
        self._tabShipData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabShipData.newOrderColumns)
            .rename(LANGUAGE_JSON['SPREADSHEET'][self._tabShipData.type]["COLUMNS"])
            .build()
        )
        return self

    def build(self):
        return self._tabShipData
