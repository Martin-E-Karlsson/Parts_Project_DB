import model.repository.product_repo as pr


def insert_product(name, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered=None, delivery_date=None):
    pr.insert_product(name, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered, delivery_date)


def get_all_products():
    return pr.get_all_products()


def get_product_by_id(product_id):
    return pr.get_product_by_id(product_id)


def get_all_products_by_attribute(attribute_name, value):
    products = pr.get_all_products_by_attribute(attribute_name, value)
    return {i+1: product for i, product in enumerate(products)}


def change_product_attribute(product_id, attribute_name, new_value):
    pr.change_product_attribute(product_id, attribute_name, new_value)


def add_retailer_to_product(product_id, retailer_name, retailer_id):
    pr.add_retailer_to_product(product_id, retailer_name, retailer_id)