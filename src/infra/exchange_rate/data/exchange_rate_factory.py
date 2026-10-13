from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 

from infra.enum.exchange_rate import ExchangeRate
from .product_class import ProductDataBuild

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRateDataFactory:
    def create(self):
        ExchangeRateDB = CONFIGURATION_JSON["DATABASE"]

        if ExchangeRateDB == ExchangeRate.LOCAL.:
            return (
                ProductDataBuild()
                .setFigureName(product_info["Nome_Figure"])
                .build()
            )
        
        elif ExchangeRateDB == ExchangeRate.SQL:
            ## Its needed to develop a sql solution here
            return

        elif ExchangeRateDB == None:
            return

        else:
            raise ValueError(
                "There is no valid value in 'database' key on 'configuration.json'"
            )
