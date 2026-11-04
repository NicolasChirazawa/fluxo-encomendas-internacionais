from application.language.read_language import read_language_JSON
from application.configuration.read_configuration import read_configuration_JSON

from enum import Enum

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON["LOCALE"]["LANGUAGE"])

class ShipStatus(Enum):
    NO_DATA          = LANGUAGE_JSON["STATUS"]["SHIP"]["NO_DATA"]
    AWAITING_PAYMENT = LANGUAGE_JSON["STATUS"]["SHIP"]["AWAITING_PAYMENT"]
    COMPLETED        = LANGUAGE_JSON["STATUS"]["SHIP"]["COMPLETED"]
