from infra.exchange_rate.exchange_rate_class import ExchangeRateBuild
from domain.ship.ship_enum import ShipStatus 

from infra.helper.fraction_product_box_price import fraction_product_box_price

class ProductShip:
    def __init__(self):
        self.shipDateLimit          = None
        self.shipCountry            = None
        self.shipDate               = None
        self.shipCurrencyPrice      = None
        self.shipCurrencyServiceTax = 0
        self.shipPaymentMethod      = None
        self.shipQuote              = None
        self.shipPrice              = None
        self.shipStatus             = ShipStatus.NO_DATA

class ProductShipBuild:
    def __init__(self):
        self._productShip = ProductShip()

    def setShipDateLimit(self, ship_date_limit):        
        self._productShip.shipDateLimit = ship_date_limit
        self._productShip.shipStatus = ShipStatus.AWAITING_PAYMENT
        return self

    def setShipCountry(self, ship_country):        
        self._productShip.shipCountry = ship_country
        return self

    def setShipDate(self, ship_date):
        self._productShip.shipDate = ship_date
        self._productShip.shipStatus = ShipStatus.COMPLETED
        return self

    def setShipCurrencyPrice(self, ship_currency_price, product_list):
        product_amout = len(product_list)

        new_ship_currency_price = fraction_product_box_price(ship_currency_price, product_amout)

        self._productShip.shipCurrencyPrice = new_ship_currency_price
        return self

    def setShipCurrencyServiceTax(self, ship_currency_service_tax, product_list):
        product_amout = len(product_list)

        new_currency_service_tax = fraction_product_box_price(ship_currency_service_tax, product_amout)

        self._productShip.shipCurrencyServiceTax = new_currency_service_tax
        return self

    def setShipPaymentMethod(self, ship_payment_method):
        self._productShip.shipPaymentMethod = ship_payment_method
        return self

    def setShipQuote(self):
        exchangeRateData = (ExchangeRateBuild()
            .setDate(self._productShip.shipDate)
            .setOriginCurrency()
            .setShipCurrency(self._productShip.shipCountry)
            .setExchangeRate()
            .build()
        )
        self._productShip.shipQuote = exchangeRateData.exchangeRate
        return self

    def setShipPrice(self):
        ## Considerar aumento por método de pagamento

        calculate_price = ((                            
            int(self._productShip.shipCurrencyPrice) + 
            int(self._productShip.shipCurrencyServiceTax)
            ) * self._productShip.shipQuote 
        ) 

        self._productShip.shipPrice = round(calculate_price, 2)
        return self

    def updateShipStatus(self, shipStatus):
        self._productShip.shipStatus = shipStatus.value
        return self

    def build(self):
        self.updateShipStatus(self._productShip.shipStatus)
        self.validate()
        return self._productShip.__dict__

    def validate(self):
        if self._productShip.shipStatus == ShipStatus.NO_DATA.value:
            return
        elif self._productShip.shipStatus == ShipStatus.AWAITING_PAYMENT.value:
            self.validateNonEmptyValues(["shipDateLimit"])
        elif self._productShip.shipStatus == ShipStatus.COMPLETED.value:
            self.validateNonEmptyValues([
                "shipDateLimit", 
                "shipCountry", 
                "shipDate", 
                "shipCurrencyPrice", 
                "shipPaymentMethod", 
                "shipPaymentMethod", 
                "shipQuote", 
                "shipPrice"
            ])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productShip, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
