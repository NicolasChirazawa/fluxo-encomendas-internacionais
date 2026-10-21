from .tax_enum import TaxStatus

from infra.helper.reduce_fraction_price import reduce_fraction_price

class ProductTax:
    def __init__(self):
        self.taxDateLimit = None
        self.taxDate      = None
        self.taxPrice     = 0
        self.taxStatus    = TaxStatus.NO_DATA

class ProductTaxBuild:
    def __init__(self):
        self._productTax = ProductTax()

    def setDateLimit (self, tax_date_limit):        
        self._productTax.taxDateLimit = tax_date_limit
        self._productTax.taxStatus = TaxStatus.AWAITING_PAYMENT
        return self
    
    def setTaxDate (self, tax_date):        
        self._productTax.taxDate = tax_date
        self._productTax.taxStatus = TaxStatus.COMPLETED
        return self

    def setTaxPrice (self, tax_price):
        new_tax_price = reduce_fraction_price(tax_price)  
        self._productTax.taxPrice = new_tax_price
        return self

    def updateTaxStatus (self, tax_status):
        self._productTax.taxStatus = tax_status.value
        return self

    def build (self):
        self.updateTaxStatus(self._productTax.taxStatus)
        self.validate()
        return self._productTax.__dict__

    def validate (self):
        if self._productTax.taxStatus == TaxStatus.NO_DATA.value:
            return
        elif self._productTax.taxStatus == TaxStatus.AWAITING_PAYMENT.value:
            self.validateNonEmptyValues(["taxDateLimit"])
        elif self._productTax.taxStatus == TaxStatus.COMPLETED.value:
            self.validateNonEmptyValues(["taxDateLimit", "taxDate", "taxPrice"])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productTax, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
