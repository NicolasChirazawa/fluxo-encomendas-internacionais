from application.configuration.read_configuration import read_configuration_JSON

CONFIGURATION_JSON = read_configuration_JSON()

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

        format_array = self._dateObject.format.split(self._dateObject.separator)
        self.validateFormat("date", format_array)
        
        self._dateObject.date = date
        return self

    def setElementsDate(self):
        acronym = {
            "dd": "day",
            "mm": "month",
            "yyyy": "year"
        }

        date_array = self._dateObject.date.split(self._dateObject.separator)
        self.validateFormat("date", date_array)
        format_array = self._dateObject.format.split(self._dateObject.separator)
        self.validateFormat("format", format_array)

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
            propertyValue = getattr(self._dateObject, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")

    def validateFormat (self, nameProperty, valueProperty):
        if len(valueProperty) != 3:
            raise ValueError(nameProperty + " has an invalid date format")
