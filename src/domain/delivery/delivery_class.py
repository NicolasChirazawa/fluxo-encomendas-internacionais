from domain.delivery.delivery_enum import DeliveryStatus

class ProductDelivery:
    def __init__ (self):
        self.deliveryDate = None
        self.deliveryStatus = DeliveryStatus.NO_DATA

class ProductDeliveryBuild:
    def __init__ (self):
        self._productDelivery = ProductDelivery()

    def setDeliveryRegister (self):
        self._productDelivery.deliveryStatus = DeliveryStatus.AWAITING_DELIVERY
        return self
    
    def setDeliveryDate (self, deliveryDate):
        self._productDelivery.deliveryDate = deliveryDate
        self._productDelivery.deliveryStatus = DeliveryStatus.COMPLETED
        return self

    def updateDeliveryStatus (self, deliveryStatus):
        self._productDelivery.deliveryStatus = deliveryStatus.value
        return self

    def build (self):
        self.updateDeliveryStatus(self._productDelivery.deliveryStatus)
        self.validate()
        return self._productDelivery.__dict__

    def validate (self):

        if self._productDelivery.deliveryStatus == DeliveryStatus.NO_DATA.value:
            return
        elif self._productDelivery.deliveryStatus == DeliveryStatus.AWAITING_DELIVERY.value:
            return
        elif self._productDelivery.deliveryStatus == DeliveryStatus.COMPLETED.value:
            self.validateNonEmptyValues(["deliveryDate"])
        else:
            raise ValueError("Invalid status error")

    def validateNonEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productDelivery, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
