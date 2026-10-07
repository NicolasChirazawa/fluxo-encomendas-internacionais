from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

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

    def setDataframe (self, data, language):
        self._tabDeliveryData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabDeliveryData.newOrderColumns)
            .rename(language['SPREADSHEET_RENAME'][self._tabDeliveryData.type])
            .build()
        )
        return self

    def build(self):
        return self._tabDeliveryData
