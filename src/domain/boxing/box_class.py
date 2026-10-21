from .box_enum import BoxStatus

class Box:
    def __init__ (self):
        self.boxCode              = None
        self.boxData              = None
        self.productPriceFraction = None
        self.boxStatus            = BoxStatus.AWAITING_BOXING

class BoxBuild:
    def __init__ (self):
        self._box = Box()

    def setBoxCode (self, box_code):
        self._box.boxCode = box_code
        return self
    
    def setBoxData (self, box_data):
        self._box.boxData = box_data
        self._box.boxStatus = BoxStatus.COMPLETED
        return self

    def setProductPriceFraction (self, product_list):

        product_price_fraction = 1 / len(product_list)
        self._box.productPriceFraction = round(product_price_fraction, 2)
        
        return self

    def updateBoxStatus (self, box_status):
        self._box.boxStatus = box_status.value
        return self

    def build (self):
        self.updateBoxStatus(self._box.boxStatus)
        self.validate()
        return self._box.__dict__

    def validate (self):
        if self._box.boxStatus == BoxStatus.AWAITING_BOXING.value:
            return
        elif self._box.boxStatus == BoxStatus.COMPLETED.value:
            self.validateNonEmptyValues(["boxCode", "boxData", "productFraction"])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._box, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
