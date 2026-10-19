import pandas as pd


class ExcelReportBuilder:
    def __init__(self):
        self._tabs = []
        self.fileName = ""

    def addTabs(self, tabs):
        self._tabs.extend(tabs)
        return self

    def addFileName(self, file_name):
        self.fileName = file_name
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