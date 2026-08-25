from .tax_enum import TaxStatus

class ProductTax:
    def __init__(self):
        self.taxDateLimit = None
        self.taxDate      = None
        self.taxPrice     = "0"
        self.taxStatus    = TaxStatus.NO_DATA

class ProductTaxBuild:
    def __init__(self):
        self._productTax = ProductTax()

    def setDateLimit (self, taxDateLimit):        
        self._productTax.taxDateLimit = taxDateLimit
        self.updateTaxStatus(TaxStatus.AWAITING_PAYMENT)
        return self
    
    def setTaxDate (self, taxDate):        
        self._productTax.taxDate = taxDate
        self.updateTaxStatus(TaxStatus.COMPLETED)
        return self

    def setTaxPrice (self, taxPrice):        
        self._productTax.taxPrice = taxPrice
        return self

    def updateTaxStatus (self, taxStatus):
        self._productTax.taxStatus = taxStatus
        return self

    def build (self):
        self.validate()
        return self._productTax.__dict__

    def validate (self):
        if self._productTax.taxStatus == TaxStatus.NO_DATA:
            return
        elif self._productTax.taxStatus == TaxStatus.AWAITING_PAYMENT:
            self.validateEmptyValues(["taxDateLimit"])
        elif self._productTax.taxStatus == TaxStatus.COMPLETED:
            self.validateEmptyValues(["taxDateLimit", "taxDate", "taxPrice"])
        else:
            raise ValueError("Invalid status error")

    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productTax, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
