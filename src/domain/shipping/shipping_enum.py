from enum import Enum

class ShippingStatus(Enum):
    NO_DATA = "No information"
    AWAITING_PAYMENT = "Awaiting payment"
    COMPLETED = "Shippment payed"
