from enum import Enum

class Status(Enum):
    NO_DATA = 'Sem informações'
    AWAITING_PAYMENT = 'Esperando pagamento'
    COMPLETED = 'Taxa de imposto foi paga'

class ProductTax:
    def __init__(self):
        self.dateLimit = ''
        self.taxDate = ''
        self.taxPrice = ''
        self.status = Status.NO_DATA

class ProductTaxBuild:
    def __init__(self):
        self._productTax = ProductTax()

    def setDateLimit(self, dateLimit):        
        self._productTax.dateLimit = dateLimit
        self.updateStatus(Status.AWAITING_PAYMENT)
        return self
    
    def setTaxDate(self, taxDate):        
        self._productTax.taxDate = taxDate
        self.updateStatus(Status.COMPLETED)
        return self

    def setTaxPrice(self, taxPrice):        
        self._productTax.taxPrice = taxPrice
        return self

    def updateStatus(self, status):
        self._productTax.status = status
        return self

    def build(self):
        self.validate()
        return self._productTax.__dict__

    def validate(self):
        if self._productTax.status == Status.NO_DATA:
            return
        elif self._productTax.status == Status.AWAITING_PAYMENT:
            self.validateEmptyValues(["dateLimit"])
        elif self._productTax.status == Status.COMPLETED:
            self.validateEmptyValues(["dateLimit", "taxDate", "taxPrice"])
        else:
            raise ValueError("Invalid status error")

    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productTax, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
