import os
from infra.json.read_json import readJSON 

def read_configuration_JSON ():
    CONFIGURATION_JSON = readJSON(os.path.join(os.path.abspath(""), "application", "configuration", "configuration.json"))
    return CONFIGURATION_JSON