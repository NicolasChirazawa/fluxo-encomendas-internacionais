from domain.delivery.delivery_enum import DeliveryStatus

class ProductDelivery:
    def __init__ (self):
        self.deliveryDate = None
        self.deliveryStatus = DeliveryStatus.NO_DATA

class ProductDeliveryBuild:
    def __init__ (self):
        self._productDelivery = ProductDelivery()

    def setDeliveryRegister (self):
        self.updateDeliveryStatus(DeliveryStatus.AWAITING_DELIVERY)
        return self
    
    def setDeliveryDate (self, deliveryDate):
        self._productDelivery.deliveryDate = deliveryDate
        self.updateDeliveryStatus(DeliveryStatus.COMPLETED)
        return self

    def updateDeliveryStatus (self, deliveryStatus):
        self._productDelivery.deliveryStatus = deliveryStatus
        return self

    def build (self):
        self.validate()
        return self._productDelivery.__dict__

    def validate (self):

        if self._productDelivery.deliveryStatus == DeliveryStatus.NO_DATA:
            return
        elif self._productDelivery.deliveryStatus == DeliveryStatus.AWAITING_DELIVERY:
            return
        elif self._productDelivery.deliveryStatus == DeliveryStatus.COMPLETED:
            self.validateEmptyValues(["deliveryDate"])
        else:
            raise ValueError("Invalid status error")

    def validateEmptyValues (self, nameProperties):
        for nameProperty in nameProperties:
            propertyValue = getattr(self._productDelivery, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")
