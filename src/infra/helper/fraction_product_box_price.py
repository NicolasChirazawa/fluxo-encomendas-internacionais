def fraction_product_box_price (price, amount):

    try:
        price = float(price)
    except:
        print("Value isnt a number")
        raise Exception

    fraction_product_box_price = price / amount
    return round(fraction_product_box_price, 2)
