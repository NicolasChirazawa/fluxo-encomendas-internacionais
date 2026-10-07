from infra.object_value.spreadsheet_template import SpreadsheetTemplateBuild

class TabSummatizedData:
    def __init__(self):
        self.type = ""
        self.tabName = ""
        self.newOrderColumns = [
            "code", 
            "figureName", 
            "status",
            "statusData"
        ] 
        self.dataframe = ""

class TabSummarizedDataBuild:
    def __init__(self):
        self._tabSumarizedData = TabSummatizedData()

    def setType (self, type):
        self._tabSumarizedData.type = type
        return self

    def setTabName (self, tabName):
        self._tabSumarizedData.tabName = tabName
        return self

    def setDataframe (self, data, language):
        self._tabSumarizedData.dataframe = (
            SpreadsheetTemplateBuild()
            .setSpreadsheetTemplate(data)
            .order(self._tabSumarizedData.newOrderColumns)
            .rename(language['SPREADSHEET_RENAME'][self._tabSumarizedData.type])
            .build()
        )
        return self

    def build(self):
        return self._tabSumarizedData
