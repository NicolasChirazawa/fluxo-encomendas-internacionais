from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['language'])

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

    def setDataframe (self, data):
        self._tabTaxData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabTaxData.newOrderColumns)
            .rename(LANGUAGE_JSON['SPREADSHEET'][self._tabTaxData.type]["COLUMNS"])
            .build()
        )
        return self

    def build(self):
        return self._tabTaxData
