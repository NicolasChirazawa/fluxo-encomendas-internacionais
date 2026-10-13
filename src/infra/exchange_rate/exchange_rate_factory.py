from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 

from infra.enum.exchange_rate import ExchangeRate
from .product_class import ProductDataBuild

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRateMethodFactory:
    def getData(self):
        ExchangeRateMethod = CONFIGURATION_JSON["DATABASE"]

        if ExchangeRateMethod == ExchangeRate.LOCAL:
            return (
                ProductDataBuild()
                .setFigureName(product_info["Nome_Figure"])
                .build()
            )
        
        elif ExchangeRateDB == ExchangeRate.SQL:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateDB == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'database' key on 'configuration.json'"
            )
    
    def setData(self, exchangeRate):
        ExchangeRateMethod = CONFIGURATION_JSON["DATABASE"]

        if ExchangeRateMethod == ExchangeRate.LOCAL:
            return (
                ProductDataBuild()
                .setFigureName(product_info["Nome_Figure"])
                .build()
            )
        
        elif ExchangeRateDB == ExchangeRate.SQL:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateDB == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'database' key on 'configuration.json'"
            )
