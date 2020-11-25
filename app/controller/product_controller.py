import model.repository.product_repo as pr


def insert_product(name, retailer, description, purchase_cost, sell_price, id_source, id_warehouse):
    pr.insert_product(name, retailer, description, purchase_cost, sell_price, id_source, id_warehouse)


def get_all_products():
    return pr.get_all_products()


def get_product_by_id(id_product):
    return pr.get_product_by_id(id_product)


def get_all_products_with_name(name):
    products = pr.get_all_products_with_name(name)
    return {i+1: product for i, product in enumerate(products)}


def change_product_name(product, new_name):
    pr.change_product_name(product, new_name)
