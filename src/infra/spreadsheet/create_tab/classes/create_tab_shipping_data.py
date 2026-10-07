from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

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
        self._tabFullData = TabShippingData()

    def setType (self, type):
        self._tabFullData.type = type
        return self

    def setTabName (self, tabName):
        self._tabFullData.tabName = tabName
        return self

    def setDataframe (self, data, language):
        self._tabFullData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabFullData.newOrderColumns)
            .rename(language['SPREADSHEET_RENAME'][self._tabFullData.type])
            .build()
        )
        return self

    def build(self):
        return self._tabFullData
