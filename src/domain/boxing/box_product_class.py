from .box_enum import BoxStatus

class ProductBox:
    def __init__ (self):
        self.boxCode     = None
        self.boxStatus   = BoxStatus.AWAITING_BOXING

class ProductBoxBuild:
    def __init__ (self):
        self._productBox = ProductBox()

    def setBoxCode (self, box_code):
        self._productBox.boxCode = box_code
        self._productBox.boxStatus = BoxStatus.COMPLETED
        return self

    def updateBoxStatus (self, box_status):
        self._productBox.boxStatus = box_status.value
        return self

    def build (self):
        self.updateBoxStatus(self._productBox.boxStatus)
        self.validate()
        return self._productBox.__dict__

    def validate (self):
        if self._productBox.boxStatus == BoxStatus.AWAITING_BOXING.value:
            return
        elif self._productBox.boxStatus == BoxStatus.COMPLETED.value:
            self.validateNonEmptyValues(["boxCode"])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productBox, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
