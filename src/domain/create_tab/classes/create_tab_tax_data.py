from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

class TabTaxData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName",
            "taxDateLimit", 
            "taxDate", 
            "taxPrice", 
            "taxStatus"
        ]
        self.dataframe = ""

class TabTaxDataBuilder:
    def __init__(self):
        self._tabTaxData = TabTaxData()

    def setType (self, type):
        self._tabTaxData.type = type
        return self

    def setTabName (self, tabName):
        self._tabTaxData.tabName = tabName
        return self

    def setDataframe (self, data, language):
        self._tabTaxData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabTaxData.newOrderColumns)
            .rename(language['SPREADSHEET_RENAME'][self._tabTaxData.type])
            .build()
        )
        return self

    def build(self):
        return self._tabTaxData
