from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type: str):
    product = [
        product
        for product in products
        if product["type"] == type
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
