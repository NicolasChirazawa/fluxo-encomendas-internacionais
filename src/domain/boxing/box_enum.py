from application.language.read_language import read_language_JSON
from application.configuration.read_configuration import read_configuration_JSON

from enum import Enum

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON["LOCALE"]["LANGUAGE"])

class BoxStatus(Enum):
    AWAITING_BOXING = LANGUAGE_JSON["STATUS"]["BOXING"]["AWAITING_BOXING"]
    COMPLETED       = LANGUAGE_JSON["STATUS"]["BOXING"]["COMPLETED"]
