import model.repository.product_repo as pr


def insert_product(name, retailer, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered=None, delivery_date=None):
    pr.insert_product(name, retailer, description, purchase_cost, sell_price, product_in_stock, minimal_stock_amount, manufacturer_id, amount_ordered, delivery_date)



def get_all_products():
    return pr.get_all_products()


def get_product_by_id(id_product):
    return pr.get_product_by_id(_id=id_product)


def get_all_products_by_attribute(attribute_name, value):
    try:
       return pr.find(**{attribute_name, value})
    except ValueError:
        print(f"The attribute_name; {attribute_name} was incorrect.")



def change_product_name(product_id, attribute_name, new_value):
    try:
        pr.change_product_name(product_id,attribute_name, new_value)
    except ValueError:
        print('Incorrect argument entered')


def insert_retailer_to_product(product_id, retailer_name, retailer_id):
    pr.push_to_embedded_list(product_id, 'retailers',{'retailer_name': retailer_name, 'retailer_id':retailer_id})


def change_product_attribute(product_id, attribute_name, new_value):
    pr.change_product_attribute(product_id, attribute_name, new_value)