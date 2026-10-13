from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

import pandas as pd

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['LANGUAGE'])

class ExcelReportBuilder:
    def __init__(self):
        self._tabs = []
        self.fileName = ""

    def addTabs(self, tabs):
        self._tabs.extend(tabs)
        return self

    def addFileName(self):
        self.fileName = LANGUAGE_JSON["SPREADSHEET"]["FILE_NAME"]
        return self

    def build(self):
        with pd.ExcelWriter(
            self.fileName + ".xlsx",
            engine="openpyxl"
        ) as writer:

            for tab in self._tabs:
                tab.dataframe.to_excel(
                    writer,
                    sheet_name=tab.tabName,
                    index=False
                )

        return