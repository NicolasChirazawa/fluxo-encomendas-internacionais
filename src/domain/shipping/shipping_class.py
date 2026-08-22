from domain.exchange_rate.exchange_rate_class import ExchangeRateDataBuild
from enum import Enum

class Status(Enum):
    NO_DATA = 'Sem informações'
    AWAITING_PAYMENT = 'Esperando pagamento'
    COMPLETED = 'Taxa de imposto foi paga'

class ProductShipping:
    def __init__(self):
        self.dateLimit = ''
        self.shippingDate = ''
        self.ienPrice = ''
        self.ienServiceTax = ''
        self.paymentMethod = ''
        self.quote = ''
        self.shippingPrice = ''
        self.status = Status.NO_DATA

class ProductShippingBuild:
    def __init__(self):
        self._productShipping = ProductShipping()

    def setDateLimit(self, dateLimit):        
        self._productShipping.dateLimit = dateLimit
        self.updateStatus(Status.AWAITING_PAYMENT)
        return self

    def setShippingDate(self, shippingDate):
        self._productShipping.shippingDate = shippingDate
        self.updateStatus(Status.COMPLETED)
        return self

    def setIenPrice(self, ienPrice):
        self._productShipping.ienPrice = ienPrice
        return self

    def setIenServiceTax(self, ienServiceTax):
        self._productShipping.ienServiceTax = ienServiceTax
        return self

    def setPaymentMethod(self, paymentMethod):
        self._productShipping.paymentMethod = paymentMethod
        return self

    def setQuote(self):
        exchangeRateData = (ExchangeRateDataBuild()
            .setDate(self._productShipping.shippingDate)
            .setExchangeRate()
            .build()
        )
        self._productShipping.quote = exchangeRateData.exchangeRate
        return self

    def setShippingPrice(self):
        ## Considerar aumento por método de pagamento

        self._productShipping.shippingPrice = (
            int(self._productShipping.ienPrice) + int(self._productShipping.ienServiceTax)
            ) * self._productShipping.quote 
        return self

    def updateStatus(self, status):
        self._productShipping.status = status
        return self

    def build(self):
        self.validate()
        return self._productShipping.__dict__

    def validate(self):
        if self._productShipping.status == Status.NO_DATA:
            return
        elif self._productShipping.status == Status.AWAITING_PAYMENT:
            self.validateEmptyValues(["dateLimit"])
        elif self._productShipping.status == Status.COMPLETED:
            self.validateEmptyValues(["dateLimit", "shippingDate", "ienPrice", "ienServiceTax", "paymentMethod", "quote", "shippingPrice"])
        else:
            raise ValueError("Invalid status error")


    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productShipping, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
