import copy

def getIdentifierData (product_data, code):
    identifier = {
        "code": code,
        "figureName": product_data["figureName"]
    }
    return identifier

def injectIdentifier (object, identifier):
    newObject = copy.deepcopy(object)

    for key in identifier:
        newObject[key] = identifier[key]

    return newObject
