from infra.exchange_rate.exchange_rate_class import ExchangeRateDataBuild

class ProductPurchase:
    def __init__(self):
        self.purchasePlace = None
        self.purchaseCountry = None
        self.purchasePaymentDate = None
        self.purchaseCurrencyPrice = None
        self.purchaseCurrencyServiceTax = 0
        self.purchasePaymentMethod = None
        self.purchaseQuote = None
        self.purchasePrice = None

class ProductPurchaseBuild:
    def __init__(self):
        self._productPurchase = ProductPurchase()

    def setPurchasePlace(self, purchasePlace):
        self._productPurchase.purchasePlace = purchasePlace
        return self

    def setPurchaseCountry(self, purchaseCountry):
        self._productPurchase.purchaseCountry = purchaseCountry
        return self

    def setPurchasePaymentDate(self, purchasePaymentDate):
        self._productPurchase.purchasePaymentDate = purchasePaymentDate
        return self

    def setPurchaseCurrencyPrice(self, purchaseCurrencyPrice):
        self._productPurchase.purchaseCurrencyPrice = purchaseCurrencyPrice
        return self

    def setPurchaseCurrencyServiceTax(self, purchaseCurrencyServiceTax):
        self._productPurchase.purchaseCurrencyServiceTax = purchaseCurrencyServiceTax
        return self

    def setPurchasePaymentMethod(self, purchasePaymentMethod):
        self._productPurchase.purchasePaymentMethod = purchasePaymentMethod
        return self

    def setPurchaseQuote(self):
        exchangeRateData = (ExchangeRateDataBuild()
            .setDate(self._productPurchase.purchasePaymentDate)
            .setCurrency(self._productPurchase.purchaseCountry)
            .setExchangeRate()
            .build()
        )
        self._productPurchase.purchaseQuote = exchangeRateData.exchangeRate
        return self

    def setPurchasePrice(self):
        ## Considerar aumento por método de pagamento

        calculate_price = ((                            
            int(self._productPurchase.purchaseCurrencyPrice) + 
            int(self._productPurchase.purchaseCurrencyServiceTax)
            ) * self._productPurchase.purchaseQuote 
        ) 

        self._productPurchase.purchasePrice = round(calculate_price, 2) 
        return self

    def build(self):
        self.validate()
        return self._productPurchase.__dict__

    def validate(self):
        self.validateEmptyValues([
            "purchasePlace", 
            "purchaseCountry", 
            "purchasePaymentDate", 
            "purchaseCurrencyPrice", 
            "purchaseCurrencyServiceTax", 
            "purchasePaymentMethod", 
            "purchaseQuote", 
            "purchasePrice"
        ])

    def validateEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productPurchase, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
