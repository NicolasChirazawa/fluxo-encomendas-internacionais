from infra.exchange_rate.exchange_rate_class import ExchangeRateBuild
from .purchase_enum import PurchaseStatus

class ProductPurchase:
    def __init__(self):
        self.purchasePlace              = None
        self.purchaseCountry            = None
        self.purchasePaymentDate        = None
        self.purchaseCurrencyPrice      = None
        self.purchaseCurrencyServiceTax = 0
        self.purchasePaymentMethod      = None
        self.purchaseQuote              = None
        self.purchasePrice              = None
        self.purchaseStatus             = PurchaseStatus.NO_DATA

class ProductPurchaseBuild:
    def __init__(self):
        self._productPurchase = ProductPurchase()

    def setPurchasePlace(self, purchase_place):
        self._productPurchase.purchasePlace = purchase_place
        return self

    def setPurchaseCountry(self, purchase_country):
        self._productPurchase.purchaseCountry = purchase_country
        return self

    def setPurchasePaymentDate(self, purchase_payment_date):
        self._productPurchase.purchasePaymentDate = purchase_payment_date
        return self

    def setPurchaseCurrencyPrice(self, purchase_currency_price):
        self._productPurchase.purchaseCurrencyPrice = purchase_currency_price
        self._productPurchase.purchaseStatus = PurchaseStatus.AWAITING_PAYMENT
        return self

    def setPurchaseCurrencyServiceTax(self, purchase_currency_service_tax):
        self._productPurchase.purchaseCurrencyServiceTax = purchase_currency_service_tax
        return self

    def setPurchasePaymentMethod(self, purchase_payment_method):
        self._productPurchase.purchasePaymentMethod = purchase_payment_method
        return self

    def setPurchaseQuote(self):
        exchangeRateData = (ExchangeRateBuild()
            .setDate(self._productPurchase.purchasePaymentDate)
            .setOriginCurrency()
            .setShippingCurrency(self._productPurchase.purchaseCountry)
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
        self._productPurchase.purchaseStatus = PurchaseStatus.COMPLETED
        return self

    def build(self):
        self.updatePurchaseStatus(self._productPurchase.purchaseStatus)
        self.validate()
        return self._productPurchase.__dict__

    def updatePurchaseStatus (self, purchaseStatus):
        self._productPurchase.purchaseStatus = purchaseStatus.value
        return self

    def validate (self):
        if self._productPurchase.purchaseStatus == PurchaseStatus.NO_DATA.value:
            return
        elif self._productPurchase.purchaseStatus == PurchaseStatus.AWAITING_PAYMENT.value:
            self.validateNonEmptyValues(["purchasePlace", "purchaseCountry", "purchaseCurrencyPrice"])
        elif self._productPurchase.purchaseStatus == PurchaseStatus.COMPLETED.value:
            self.validateNonEmptyValues([
                "purchasePlace", 
                "purchaseCountry", 
                "purchasePaymentDate", 
                "purchaseCurrencyPrice", 
                "purchaseCurrencyServiceTax", 
                "purchasePaymentMethod", 
                "purchaseQuote", 
                "purchasePrice"
            ])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productPurchase, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
