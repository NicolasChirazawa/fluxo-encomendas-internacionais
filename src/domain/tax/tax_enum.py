from enum import Enum

class TaxStatus(Enum):
    NO_DATA = "Sem informações"
    AWAITING_PAYMENT = "Esperando pagamento"
    COMPLETED = "Taxa de imposto foi paga"
