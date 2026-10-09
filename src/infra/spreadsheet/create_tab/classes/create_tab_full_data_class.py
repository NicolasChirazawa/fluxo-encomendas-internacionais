from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['language'])

class TabFullData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName", 
            "mfcLink", 
            "brand", 
            "productLine", 
            "scale",
            "purchasePlace", 
            "purchasePaymentDate", 
            "purchaseCurrencyPrice", 
            "purchaseCurrencyServiceTax", 
            "purchasePaymentMethod", 
            "purchaseQuote", 
            "purchasePrice",
            "shippingDateLimit", 
            "shippingCountry", 
            "shippingDate", 
            "shippingCurrencyPrice", 
            "shippingCurrencyServiceTax", 
            "shippingPaymentMethod", 
            "shippingQuote", 
            "shippingPrice", 
            "shippingStatus",
            "taxDateLimit", 
            "taxDate", 
            "taxPrice", 
            "taxStatus",
            "deliveryDate",
            "deliveryStatus"
        ] 
        self.dataframe = ""

class TabFullDataBuild:
    def __init__(self):
        self._tabFullData = TabFullData()

    def setType (self, type):
        self._tabFullData.type = type
        return self

    def setTabName (self, tabName):
        self._tabFullData.tabName = tabName
        return self

    def setDataframe (self, data):
        self._tabFullData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabFullData.newOrderColumns)
            .rename(LANGUAGE_JSON['SPREADSHEET'][self._tabFullData.type]["COLUMNS"])
            .build()
        )
        return self

    def build(self):
        return self._tabFullData
