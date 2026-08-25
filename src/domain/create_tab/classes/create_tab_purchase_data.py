from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

class TabPurchaseData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName",
            "purchasePlace", 
            "purchasePaymentDate", 
            "purchaseCurrencyPrice", 
            "purchaseCurrencyServiceTax", 
            "purchasePaymentMethod", 
            "purchaseQuote", 
            "purchasePrice"
        ]
        self.dataframe = ""

class TabPurchaseDataBuilder:
    def __init__(self):
        self._tabFullData = TabPurchaseData()

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
