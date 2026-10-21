def searchProductBox(product_code, boxes):
    box_data = None
    box_code = None

    for code in boxes:
        if product_code in boxes[code]["PRODUTOS"]:
            box_data = boxes[code]
            box_code = code
            break

    if (box_data == None) or (box_code == None):
        return None
        
    box = {
        "BOX_DATA": box_data,
        "BOX_CODE": box_code
    }

    return box
