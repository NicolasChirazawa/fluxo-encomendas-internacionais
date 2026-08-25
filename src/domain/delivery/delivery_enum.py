from enum import Enum

class DeliveryStatus(Enum):
    NO_DATA = "Sem informações"
    AWAITING_DELIVERY = "Esperando chegar"
    COMPLETED = "Produto chegou"
