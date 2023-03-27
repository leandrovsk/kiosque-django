from menu import products


def get_product_by_id(id: int):

    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type: str):

    if type(product_type) != str:
        raise TypeError("product type must be a str")

    product = [
        product
        for product in products
        if product["type"] == product_type
    ]
    return product


def add_product(lista: list, **args):
    list_ids = [
        product["_id"]
        for product in lista
    ]

    new_id = 1

    if list_ids:
        new_id = max(list_ids) + 1

    args["_id"] = new_id

    lista.append(args)

    return args

def menu_report():

    product_count = products.__len__()

    product_sum = 0

    for product in products:
        product_sum += product["price"]

    product_types = ["vegetable", "fruit", "drink", "dairy", "bakery", "meat"]

    max_ocurr_type = ""
    max_ocurr = 0
    counter = 0

    for item_type in product_types:
        for product in products:
            if product["type"] == item_type:
                counter += 1
        if counter > max_ocurr:
            max_ocurr_type = item_type
            max_ocurr = counter
        counter = 0

    average_price = round((product_sum / product_count), 2)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {max_ocurr_type}"