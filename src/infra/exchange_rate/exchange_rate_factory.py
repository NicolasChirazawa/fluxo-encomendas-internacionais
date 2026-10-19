from application.configuration.read_configuration import read_configuration_JSON 
from application.database.read_database import read_database_JSON 

from infra.enum.exchange_rate_method import ExchangeRateMethod
from infra.exchange_rate.local import exchange_rate_cache

DATABASE_JSON      = read_database_JSON()
CONFIGURATION_JSON = read_configuration_JSON()

class ExchangeRateDataFactory:
    def get (origen_currency, shipping_currency, date_format_exchange_rate):

        ExchangeRateConfig = CONFIGURATION_JSON.get("DATABASE")
        if ExchangeRateConfig != None:
            ExchangeRateConfig = ExchangeRateConfig.upper()


        if ExchangeRateConfig == ExchangeRateMethod.LOCAL.name:
            return exchange_rate_cache.get(origen_currency, shipping_currency, date_format_exchange_rate)
        
        elif ExchangeRateConfig == ExchangeRateMethod.SQL.name:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateConfig == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'DATABASE' key on 'configuration.json'"
            )
    
    def set (origen_currency, shipping_currency, date_format_exchange_rate, exchange_rate_value):

        ExchangeRateConfig = CONFIGURATION_JSON.get("DATABASE")
        if ExchangeRateConfig != None:
            ExchangeRateConfig = ExchangeRateConfig.upper()

        if ExchangeRateConfig == ExchangeRateMethod.LOCAL.name:
            exchange_rate_cache.set(origen_currency, shipping_currency, date_format_exchange_rate, exchange_rate_value)
            return
        
        elif ExchangeRateConfig == ExchangeRateMethod.SQL.name:
            ## It’s necessary to develop a SQL database solution here.
            return None

        elif ExchangeRateConfig == None:
            return None

        else:
            raise ValueError(
                "There is no valid value in 'DATABASE' key on 'configuration.json'"
            )
