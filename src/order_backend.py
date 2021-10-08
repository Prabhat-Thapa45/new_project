from src.constants import STOCK, BQ_SIZE, YOUR_CART


def validate_entry(value):
    try:
        value = int(value)
    except ValueError:
        return None
    else:
        if value < 1:
            return None
        else:
            return value


def flower_out_of_stock(order_quantity, in_stock):
    if order_quantity > in_stock:
        return True
    else:
        return False


def bq_size_exceeded(valid_order_quantity):
    if valid_order_quantity > BQ_SIZE[0]:
        return True


def adding_to_cart(valid_order_quantity, flower_name, price):
    YOUR_CART.append({"flower_name": flower_name, "quantity": valid_order_quantity, "price": price})
    BQ_SIZE[0] -= valid_order_quantity
    return YOUR_CART, BQ_SIZE


def update_stock(flower_name, valid_order_quantity):
    for item in STOCK:
        if item['flower_name'] == flower_name:
            item['quantity'] -= valid_order_quantity


def check_order_criteria():
    if BQ_SIZE[0] == 0:
        return True


def proceed_to_buy():
    YOUR_CART.clear()
    return "Order placed successfully"
