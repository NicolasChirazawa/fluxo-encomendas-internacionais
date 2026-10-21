from application.language.read_language import read_language_JSON
from application.configuration.read_configuration import read_configuration_JSON

from enum import Enum

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON["LOCALE"]["LANGUAGE"])

class DeliveryStatus(Enum):
    NO_DATA           = LANGUAGE_JSON["STATUS"]["DELIVERING"]["NO_DATA"]
    AWAITING_DELIVERY = LANGUAGE_JSON["STATUS"]["DELIVERING"]["AWAITING_DELIVERY"]
    COMPLETED         = LANGUAGE_JSON["STATUS"]["DELIVERING"]["COMPLETED"]
