from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 

from infra.enum.exchange_rate_method import ExchangeRateMethod
from infra.exchange_rate.local import exchange_rate_cache

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRateDataFactory:
    def get (self, origenCurrency, shippingCurrency, dateFormatExchangeRate):
        ExchangeRateConfig = CONFIGURATION_JSON["DATABASE"].upper()

        if ExchangeRateConfig == ExchangeRateMethod.LOCAL.value:
            return exchange_rate_cache.get(origenCurrency, shippingCurrency, dateFormatExchangeRate)
        
        elif ExchangeRateConfig == ExchangeRateMethod.SQL.value:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateConfig == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'DATABASE' key on 'configuration.json'"
            )
    
    def set (self, origenCurrency, shippingCurrency, dateFormatExchangeRate, exchangeRate):
        ExchangeRateConfig = CONFIGURATION_JSON["DATABASE"].upper()

        if ExchangeRateConfig == ExchangeRateMethod.LOCAL.value:
            exchange_rate_cache.set(origenCurrency, shippingCurrency, dateFormatExchangeRate, exchangeRate)
            return
        
        elif ExchangeRateConfig == ExchangeRateMethod.SQL.value:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateConfig == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'DATABASE' key on 'configuration.json'"
            )
