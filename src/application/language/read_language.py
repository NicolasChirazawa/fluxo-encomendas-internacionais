import os
from infra.json.read_json import readJSON 

def read_language_JSON (language):
    LANGUAGE_JSON = readJSON(os.path.join(os.path.abspath(""), "application", "language", f"{language}.json"))
    return LANGUAGE_JSON