from infra.exchange_rate.exchange_rate_class import ExchangeRateDataBuild
from domain.shipping.shipping_enum import ShippingStatus 

class ProductShipping:
    def __init__(self):
        self.shippingDateLimit = None
        self.shippingCountry = None
        self.shippingDate = None
        self.shippingCurrencyPrice = None
        self.shippingCurrencyServiceTax = 0
        self.shippingPaymentMethod = None
        self.shippingQuote = None
        self.shippingPrice = None
        self.shippingStatus = ShippingStatus.NO_DATA

class ProductShippingBuild:
    def __init__(self):
        self._productShipping = ProductShipping()

    def setShippingDateLimit(self, shippingDateLimit):        
        self._productShipping.shippingDateLimit = shippingDateLimit
        self.updateShippingStatus(ShippingStatus.AWAITING_PAYMENT)
        return self

    def setShippingCountry(self, shippingCountry):        
        self._productShipping.shippingCountry = shippingCountry
        return self

    def setShippingDate(self, shippingDate):
        self._productShipping.shippingDate = shippingDate
        self.updateShippingStatus(ShippingStatus.COMPLETED)
        return self

    def setShippingCurrencyPrice(self, shippingCurrencyPrice):
        self._productShipping.shippingCurrencyPrice = shippingCurrencyPrice
        return self

    def setShippingCurrencyServiceTax(self, shippingCurrencyServiceTax):
        self._productShipping.shippingCurrencyServiceTax = shippingCurrencyServiceTax
        return self

    def setShippingPaymentMethod(self, shippingPaymentMethod):
        self._productShipping.shippingPaymentMethod = shippingPaymentMethod
        return self

    def setShippingQuote(self):
        exchangeRateData = (ExchangeRateDataBuild()
            .setDate(self._productShipping.shippingDate)
            .setCurrency(self._productShipping.shippingCountry)
            .setExchangeRate()
            .build()
        )
        self._productShipping.shippingQuote = exchangeRateData.exchangeRate
        return self

    def setShippingPrice(self):
        ## Considerar aumento por método de pagamento

        calculate_price = ((                            
            int(self._productShipping.shippingCurrencyPrice) + 
            int(self._productShipping.shippingCurrencyServiceTax)
            ) * self._productShipping.shippingQuote 
        ) 

        self._productShipping.shippingPrice = round(calculate_price, 2)
        return self

    def updateShippingStatus(self, shippingStatus):
        self._productShipping.shippingStatus = shippingStatus
        return self

    def build(self):
        self.validate()
        return self._productShipping.__dict__

    def validate(self):
        if self._productShipping.shippingStatus == ShippingStatus.NO_DATA:
            return
        elif self._productShipping.shippingStatus == ShippingStatus.AWAITING_PAYMENT:
            self.validateEmptyValues(["dateLimit"])
        elif self._productShipping.shippingStatus == ShippingStatus.COMPLETED:
            self.validateEmptyValues([
                "shippingDateLimit", 
                 "shippingCountry", 
                 "shippingDate", 
                 "shippingCurrencyPrice", 
                 "shippingPaymentMethod", 
                 "shippingPaymentMethod", 
                 "shippingQuote", 
                 "shippingPrice"
                ])
        else:
            raise ValueError("Invalid status error")

    def validateEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productShipping, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
