import os
import json

DATABASE_ARCHIVE = os.path.abspath('figure_data.json')

DATABASE_DATA = open(DATABASE_ARCHIVE, "r")
CONFIGURATION_JSON = json.load(DATABASE_DATA)

DATABASE_DATA.close()

class DateObjectValue:
    def __init__(self):
        self.date = ""
        self.separator = CONFIGURATION_JSON["separator"] # Format needs to be using the same separator as date
        self.format = CONFIGURATION_JSON["format"]
        self.day = ""
        self.month = ""
        self.year = ""

        
class DateObjectBuild:
    def __init__(self):
        self._dateObject = DateObjectValue()

    def setDate(self, date):    
        format_array = format.split(self._dateObject.separator)
        self.validateFormat("date", format_array)
            
        self._dateObject.date = date
        return self

    def setElementsDate(self):
        acronym = {
            'dd': 'day',
            'mm': 'month',
            'yy': 'year'
        }

        date_array = self._dateObject.date.split(self._dateObject.separator)
        self.validateFormat(self, 'date', date_array)
        format_array = self._dateObject.format.split(self._dateObject.separator)
        self.validateFormat(self, 'format', format_array)

        counter = 0

        for element in format_array:
            setattr(
                self._dateObject,
                acronym[element],
                date_array[counter]
            )
            counter += 1

        return self

    def build(self):
        self.validate()
        return self._dateObject

    def validate(self):
        # Validação de valores null
        self.validateEmptyValues(["date", "separator", "format", "day", "month", "year"])

    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productData, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")

    def validateFormat (self, nameProperty, valueProperty):
        if valueProperty.__len__ != 3:
            raise ValueError(nameProperty + " has an invalid date format")
