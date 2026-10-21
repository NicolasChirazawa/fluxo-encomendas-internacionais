from infra.exchange_rate.exchange_rate_class import ExchangeRateBuild
from domain.shipping.shipping_enum import ShippingStatus 

from infra.helper.reduce_fraction_price import reduce_fraction_price

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

    def setShippingDateLimit(self, shipping_date_limit):        
        self._productShipping.shippingDateLimit = shipping_date_limit
        self._productShipping.shippingStatus = ShippingStatus.AWAITING_PAYMENT
        return self

    def setShippingCountry(self, shipping_country):        
        self._productShipping.shippingCountry = shipping_country
        return self

    def setShippingDate(self, shipping_date):
        self._productShipping.shippingDate = shipping_date
        self._productShipping.shippingStatus = ShippingStatus.COMPLETED
        return self

    def setShippingCurrencyPrice(self, shipping_currency_price):
        new_shipping_currency_price = reduce_fraction_price(shipping_currency_price)
        self._productShipping.shippingCurrencyPrice = new_shipping_currency_price

        return self

    def setShippingCurrencyServiceTax(self, shipping_currency_service_tax):
        new_currency_service_tax = reduce_fraction_price(shipping_currency_service_tax)
        self._productShipping.shippingCurrencyServiceTax = new_currency_service_tax
        return self

    def setShippingPaymentMethod(self, shipping_payment_method):
        self._productShipping.shippingPaymentMethod = shipping_payment_method
        return self

    def setShippingQuote(self):
        exchangeRateData = (ExchangeRateBuild()
            .setDate(self._productShipping.shippingDate)
            .setOriginCurrency()
            .setShippingCurrency(self._productShipping.shippingCountry)
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
        self._productShipping.shippingStatus = shippingStatus.value
        return self

    def build(self):
        self.updateShippingStatus(self._productShipping.shippingStatus)
        self.validate()
        return self._productShipping.__dict__

    def validate(self):
        if self._productShipping.shippingStatus == ShippingStatus.NO_DATA.value:
            return
        elif self._productShipping.shippingStatus == ShippingStatus.AWAITING_PAYMENT.value:
            self.validateNonEmptyValues(["shippingDateLimit"])
        elif self._productShipping.shippingStatus == ShippingStatus.COMPLETED.value:
            self.validateNonEmptyValues([
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

    def validateNonEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productShipping, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
