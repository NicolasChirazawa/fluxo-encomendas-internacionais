from domain.exchange_rate.exchange_rate_class import ExchangeRateDataBuild

class ProductPurchase:
    def __init__(self):
        self.paymentDate = ''
        self.ienPrice = ''
        self.ienServiceTax = ''
        self.paymentMethod = ''
        self.quote = ''
        self.purchasePrice = ''

class ProductPurchaseBuild:
    def __init__(self):
        self._productPurchase = ProductPurchase()

    def setPaymentDate(self, paymentDate):        
        self._productPurchase.paymentDate = paymentDate
        return self

    def setIenPrice(self, ienPrice):
        self._productPurchase.ienPrice = ienPrice
        return self

    def setIenServiceTax(self, ienServiceTax):
        self._productPurchase.ienServiceTax = ienServiceTax
        return self

    def setPaymentMethod(self, paymentMethod):
        self._productPurchase.paymentMethod = paymentMethod
        return self

    def setQuote(self):
        exchangeRateData = (ExchangeRateDataBuild()
            .setDate(self._productPurchase.paymentDate)
            .setExchangeRate()
            .build()
        )
        self._productPurchase.quote = exchangeRateData.exchangeRate
        return self

    def setPurchasePrice(self):
        ## Considerar aumento por método de pagamento

        self._productPurchase.purchasePrice = (
            int(self._productPurchase.ienPrice) + int(self._productPurchase.ienServiceTax)
            ) * self._productPurchase.quote 
        return self

    def build(self):
        self.validate()
        return self._productPurchase.__dict__

    def validate(self):
        # Validação de valores null
        self.validateEmptyValues(["paymentDate", "ienPrice", "ienServiceTax", "paymentMethod", "quote", "purchasePrice"])

    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productPurchase, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
