from menu import products

def calculate_tab(lista: list):
    soma = 0

    for item in lista:
        item_price = [
            product["price"] * item["amount"]
            for product in products
            if product["_id"] == item["_id"]
        ]
        if item_price:
            soma += item_price[0]

    total = {'subtotal': f'${round(soma, 2)}'}

    return total