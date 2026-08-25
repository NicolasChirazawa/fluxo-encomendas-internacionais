import os
from infra.json.read_json import readJSON 

def read_database_JSON ():
    DATABASE_JSON = readJSON(os.path.join(os.path.abspath(""), "application", "database", "database.json"))
    return DATABASE_JSON