import os
import json

def readJSON (path):
    DATABASE_ARCHIVE = os.path.abspath(path)

    with open(DATABASE_ARCHIVE, "r", encoding="utf-8") as database_file:
        JSON_DATA = {}
        
        try:
            JSON_DATA = json.load(database_file)
        except:
            print("File is not a formal 'json'")

    return JSON_DATA