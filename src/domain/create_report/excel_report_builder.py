import pandas as pd

class ExcelReportBuilder:
    def __init__(self):
        self._tabs = []

    def addTabs(self, tabs):
        self._tabs.extend(tabs)
        return self

    def build(self, fileName):
        with pd.ExcelWriter(
            fileName,
            engine="openpyxl"
        ) as writer:

            for tab in self._tabs:
                tab.dataframe.to_excel(
                    writer,
                    sheet_name=tab.tabName,
                    index=False
                )

        return