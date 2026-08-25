import pandas as pd 

class SpreadsheetTemplate:
    def __init__(self):
        self.pdDataframe = None

class SpreadsheetTemplateBuild:
    def __init__(self):
        self._spreadsheat = SpreadsheetTemplate()

    def setSpreadsheetTemplate (self, array):
        pdDataframe = pd.DataFrame(array)
        self._spreadsheat.pdDataframe = pdDataframe
        return self

    def order (self, orderColumns):
        self._spreadsheat.pdDataframe = (
            self._spreadsheat.pdDataframe.loc[:, orderColumns]
        )
        return self

    def rename (self, nameColumns):
        self._spreadsheat.pdDataframe.columns = nameColumns
        return self

    def build(self):
        return self._spreadsheat.pdDataframe
