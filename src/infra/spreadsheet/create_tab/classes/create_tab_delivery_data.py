from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['language'])

class TabDeliveryData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName",
            "deliveryDate",
            "deliveryStatus",
        ]
        self.dataframe = ""

class TabDeliveryDataBuilder:
    def __init__(self):
        self._tabDeliveryData = TabDeliveryData()

    def setType (self, type):
        self._tabDeliveryData.type = type
        return self

    def setTabName (self, tabName):
        self._tabDeliveryData.tabName = tabName
        return self

    def setDataframe (self, data):
        self._tabDeliveryData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabDeliveryData.newOrderColumns)
            .rename(LANGUAGE_JSON['SPREADSHEET'][self._tabDeliveryData.type]["COLUMNS"])
            .build()
        )
        return self

    def build(self):
        return self._tabDeliveryData
