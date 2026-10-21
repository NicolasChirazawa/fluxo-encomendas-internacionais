import copy

def getIdentifierData (product_data, boxCode):
    identifier = {
        "code": boxCode,
        "figureName": product_data["figureName"]
    }
    return identifier

def injectIdentifier (object, identifier):
    newObject = copy.deepcopy(object)

    for key in identifier:
        newObject[key] = identifier[key]

    return newObject
